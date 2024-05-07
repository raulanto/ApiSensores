from django.contrib import admin

from Producto.models.ValoresProducto import ValoresProducto
from ..models.Producto import Producto
from ..filter.ProductoFilter import ProductoFilter
@admin.register(ValoresProducto)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','valorMaximo','valorMinimo','producto']
    list_filter = [ProductoFilter]
    # Vista registro
    fieldsets = (
        ('Valores', {
            'fields': ('nombre', 'valorMaximo','valorMinimo', 'producto')
        }),

    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(producto__usuario=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "producto":
            # Limit choices for the producto field to those created by the current user
            kwargs["queryset"] = Producto.objects.filter(usuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)