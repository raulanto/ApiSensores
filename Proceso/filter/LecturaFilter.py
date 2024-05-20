from ..models.LecturaEtapa import LecturaEtapa

from django.utils.translation import  gettext_lazy as _
from django.contrib import  admin


class ProcesoFilter(admin.SimpleListFilter):
    title = _('Lectura')
    parameter_name = 'lectura'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            proceso = LecturaEtapa.objects.all()
        else:
            proceso = LecturaEtapa.objects.filter(usuario=request.user)

        return [(pla.id, pla.fkESeccionEquipoSensor) for pla in proceso]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkESeccionEquipoSensor_id=self.value())