from django.contrib import admin
from .models import Organizacion

# Register your models here.
# admin.site.register(Organizacion)
@admin.register(Organizacion)
class AdminOrganizacion(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion','fkUsuario']
    list_editable = ['nombre']


    search_fields = ['nombre']
