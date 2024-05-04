from django.contrib import admin
from ..models import  Municipio


@admin.register(Municipio)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado']
    list_display_links = ['id', 'nombre']
    list_filter = ['estado']