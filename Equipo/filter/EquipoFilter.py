from ..models.Equipo import Equipo

from django.utils.translation import gettext_lazy as _
from django.contrib import admin



class EquipoFilter(admin.SimpleListFilter):
    title = _('Equipo')
    parameter_name = 'equipo'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            equipo = Equipo.objects.all()
        else:
            equipo = Equipo.objects.filter(usuario=request.user)

        return [(equ.id, equ.nombre) for equ in equipo]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(fkequipo_id=self.value())