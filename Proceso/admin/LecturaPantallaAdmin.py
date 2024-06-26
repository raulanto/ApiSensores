from django.contrib import admin
from Proceso.models import *
from ..actions.LecturaAction import descargar_valores,generar_grafico




@admin.register(LecturaEtapa)
class LecturaEtapaAdmin(admin.ModelAdmin):
    list_display = ['id', 'valor', 'fkEtapa', 'fkESeccionEquipoSensor','created_at','createdTime_at']
    actions = [descargar_valores,generar_grafico]