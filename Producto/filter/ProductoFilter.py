from ..models.Producto import Producto
from django.utils.translation import gettext_lazy as _
from django.contrib import admin


class ProductoFilter(admin.SimpleListFilter):
    title = _('Producto')
    parameter_name = 'producto'

    def lookups(self, request, model_admin):
        """
        Devuelve una lista de tuplas (valor, etiqueta) que se utilizarán para crear las opciones del filtro.
        """
        if request.user.is_superuser:
            producto = Producto.objects.all()
        else:
            producto = Producto.objects.filter(usuario=request.user)

        return [(pro.id, pro.nombre) for pro in producto]

    def queryset(self, request, queryset):
        """
        Aplica el filtro al queryset.
        """

        if self.value() is None:
            return queryset

        return queryset.filter(producto_id=self.value())