from django.contrib import admin

from Equipo.models import Equipo,SeccionEquipo,Sensores,SeccionEquipoSensor

# Register your models here.
# admin.site.register(SeccionEquipo)
admin.site.register(Sensores)


@admin.register(SeccionEquipo)
class SeccionEquipoAdmin(admin.ModelAdmin):

    list_display = ['id','nombre','fkequipo']
    list_filter = ['fkequipo']



@admin.register(SeccionEquipoSensor)
class SeccionEquipoSensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'seccion_equipo_nombre', 'sensor_nombre','nombre_equipo']
    # Relacion de varios niveles
    list_filter = ['fkseccionEquipo__fkequipo']
    def seccion_equipo_nombre(self, obj):
        return obj.fkseccionEquipo.nombre

    seccion_equipo_nombre.short_description = 'Sección del Equipo'

    def sensor_nombre(self, obj):
        return obj.fksensor.nombre

    sensor_nombre.short_description = 'Sensor'

    def nombre_equipo(self,obj):
        return obj.fkseccionEquipo.fkequipo.nombre

    nombre_equipo.short_description='Equipo'




@admin.register(Equipo)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'fkplanta']
    list_display_links = ['id', 'nombre']
    list_filter = ['fkplanta']
    list_per_page = 10

    # excluir los datos a modificar
    # exclude = ['usuario']
