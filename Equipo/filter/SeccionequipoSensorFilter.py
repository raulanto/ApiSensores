from ..models.SeccionEquipoSensor import SeccionEquipoSensor

from django.utils.translation import gettext_lazy as _
from django.contrib import admin



class SeccionEquipoSensorFilter(admin.SimpleListFilter):
    title = _('SeccionEquipoSensor')
    parameter_name = 'seccionEquipoSensor'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            seccionEquipo = SeccionEquipoSensor.objects.all()
        else:
            seccionEquipo = SeccionEquipoSensor.objects.filter(fkequipo__usuario=request.user)

        return [(equ.id, equ.fkseccionEquipo) for equ in seccionEquipo]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkESeccionEquipoSensor_id=self.value())
