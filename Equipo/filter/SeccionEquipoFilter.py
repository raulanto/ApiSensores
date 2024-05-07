from ..models.SeccionEquipo import SeccionEquipo

from django.utils.translation import gettext_lazy as _
from django.contrib import admin



class SeccionEquipoFilter(admin.SimpleListFilter):
    title = _('SeccionEquipo')
    parameter_name = 'seccionEquipo'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            seccionEquipo = SeccionEquipo.objects.all()
        else:
            seccionEquipo = SeccionEquipo.objects.filter(fkequipo__usuario=request.user)

        return [(equ.id, equ.nombre) for equ in seccionEquipo]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkequipo_id=self.value())
