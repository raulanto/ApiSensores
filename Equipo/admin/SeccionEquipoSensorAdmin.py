from Equipo.actions import exportSeccionequipoSensor_csv
from Equipo.models import SeccionEquipoSensor
from django.contrib import admin

@admin.register(SeccionEquipoSensor)
class SeccionEquipoSensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'seccion_equipo_nombre', 'sensor_nombre','nombre_equipo']
    actions = [exportSeccionequipoSensor_csv]
    # Relacion de varios niveles
    # list_filter = ['fkseccionEquipo__fkequipo']

    def seccion_equipo_nombre(self, obj):
        return obj.fkseccionEquipo.nombre

    seccion_equipo_nombre.short_description = 'Sección del Equipo'

    def sensor_nombre(self, obj):
        if obj.fksensor is not None:
            return obj.fksensor.nombre
        return None

    sensor_nombre.short_description = 'Sensor'

    def nombre_equipo(self, obj):
        return obj.fkseccionEquipo.fkequipo.nombre

    nombre_equipo.short_description = 'Equipo'
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            # Si el usuario es superusuario, mostrar todos los objetos SeccionEquipoSensor
            return queryset
        else:
            # Si el usuario no es superusuario, filtrar los objetos por el usuario actual
            return queryset.filter(fkseccionEquipo__fkequipo__usuario=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkseccionEquipo":
            # Filtrar las secciones de equipo por el usuario actual
            kwargs["queryset"] = db_field.related_model.objects.filter(fkequipo__usuario=request.user)
        elif db_field.name == "fksensor":
            # Filtrar los sensores por el usuario actual
            kwargs["queryset"] = db_field.related_model.objects.filter(usuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
