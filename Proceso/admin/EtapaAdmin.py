from django.contrib import admin
from Proceso.models import *


@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','fkestadoEtapa','fkProceso','duracion_en_horas']

