from django.contrib import admin
from .models import Planta, Municipio, Estado




admin.site.register(Estado)


@admin.register(Planta)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'usuario', 'municipio']
    list_display_links = ['id', 'nombre']
    list_filter = ['municipio']
    list_per_page = 10

    # excluir los datos a modificar
    # exclude = ['usuario']

@admin.register(Municipio)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado']
    list_display_links = ['id', 'nombre']
    list_filter = ['estado']
