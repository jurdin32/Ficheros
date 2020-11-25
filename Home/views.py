from django.shortcuts import render
from Home.models import Directory
from Home.task import directory_task



def visitfile(fullname, file, path):
    print(fullname,file,path)

def index(request):
    if request.POST:
        Directory.objects.all().delete()
        directory_task.delay(request.POST['uri'], visitfile)
    contexto={
        'all':Directory.objects.all(),
    }
    return render(request,'index.html',contexto)