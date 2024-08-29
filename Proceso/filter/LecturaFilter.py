from ..models.LecturaEtapa import LecturaEtapa

from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class ProcesoFilter(admin.SimpleListFilter):
    title = _('Lectura')
    parameter_name = 'fkESeccionEquipoSensor'

    def lookups(self, request, model_admin):
        queryset = LecturaEtapa.objects.all()
        return [(sensor.id, sensor.fkseccionEquipo.nombre) for sensor in queryset]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(fkESeccionEquipoSensor_id=self.value())
        return queryset