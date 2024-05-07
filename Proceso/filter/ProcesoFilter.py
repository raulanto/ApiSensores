from ..models.Proceso import Proceso

from django.utils.translation import  gettext_lazy as _
from django.contrib import  admin


class ProcesoFilter(admin.SimpleListFilter):
    title = _('Proceso')
    parameter_name = 'proceso'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            proceso = Proceso.objects.all()
        else:
            proceso = Proceso.objects.filter(usuario=request.user)

        return [(pla.id, pla.nombre) for pla in proceso]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkProceso_id=self.value())