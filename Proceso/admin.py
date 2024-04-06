from django.contrib import admin
from Proceso.models import *
# Register your models here.
admin.site.register(EstadoEtapa)
# admin.site.register(Etapa)
admin.site.register(Proceso)
# admin.site.register(LecturaEtapa)



@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','fkestadoEtapa','fkProceso','duracion_en_horas']



@admin.register(LecturaEtapa)
class LecturaEtapaAdmin(admin.ModelAdmin):
    list_display = ['id','valor','fkEtapa','fkESeccionEquipoSensor']








