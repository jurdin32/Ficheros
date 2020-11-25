from __future__ import absolute_import, unicode_literals

import hashlib
import os
from stat import ST_MODE, S_ISDIR, S_ISREG

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from Ficheros import settings
from Home.models import Directory

def calculo_hash(pathfile):
    f = open(pathfile, 'rb')
    sha256= hashlib.sha256()
    try:
        sha256.update(f.read())
    finally: f.close()
    result=sha256.hexdigest()
    print(pathfile,result)
    return result



@shared_task
def directory_task(uri, callback):
    for file in os.listdir(uri):
        pathname = os.path.join(uri, file)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            directory_task(pathname, callback)
            Directory(path=pathname,sha256="")
        elif S_ISREG(mode):
            callback(pathname, file, uri)
            Directory(path=pathname,sha256=calculo_hash(pathname)).save()
    print('Proceso finalizado..!')

@shared_task
def send_user_mail(archivo):
        asunto = "Error en la comprobacion de archivos"
        from_email = 'urdin32@gmail.com'
        to = 'urdin-23@live.com'
        text_content = 'Este mnsaje es importante.'
        html_content = '<p>Al parecer se han econtrado <strong>modificaciones en el archivo:</strong>  %s, se requiere atención inmediata.</p>'%(archivo.path)
        msg = EmailMultiAlternatives(asunto, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@shared_task
def test():
    directorio = Directory.objects.all()
    for direct in directorio:
        sha256=calculo_hash(direct.path)
        if direct.sha256==sha256:
            direct.verificacion=True
            direct.save()
        else:
            print("Se ha modificado el archivo:",direct.path)
            if direct.envio ==False:
                direct.verificacion = False
                direct.envio = True
                send_user_mail(direct)
                direct.save()


