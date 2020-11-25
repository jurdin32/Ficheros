from django.contrib import admin

# Register your models here.
from Home.models import Directory


@admin.register(Directory)
class AdminDirectory(admin.ModelAdmin):
    list_display_links = ['id','path','sha256','verificacion']
    list_display =  ['id','path','sha256','verificacion','envio']