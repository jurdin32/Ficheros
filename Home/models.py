from django.db import models

# Create your models here.

class Directory(models.Model):
    path=models.TextField()
    sha256=models.TextField()
    verificacion=models.BooleanField(null=True,blank=True)
    envio=models.BooleanField(default=False)