from ..models.Planta import Planta

from django.utils.translation import gettext_lazy as _
from django.contrib import admin



class PlantaFilter(admin.SimpleListFilter):
    title = _('Planta')
    parameter_name = 'planta'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            planta = Planta.objects.all()
        else:
            planta = Planta.objects.filter(usuario=request.user)

        return [(pla.id, pla.nombre) for pla in planta]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkplanta_id=self.value())