from Organizacion.models.Organizacion import Organizacion
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class OrganizacionFilter(admin.SimpleListFilter):
    title = _('Organizacion')
    parameter_name = 'organizacion'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            organizaciones = Organizacion.objects.all()
        else:
            organizaciones = Organizacion.objects.filter(fkUsuario=request.user)

        return [(org.id, org.nombre) for org in organizaciones]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(organizacion_id=self.value())
