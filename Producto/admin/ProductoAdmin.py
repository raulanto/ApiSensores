from django.contrib import admin
from django.utils.html import format_html

from Producto.models.Producto import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'display_fografiaPex', 'nombre', 'descripcion_truncada', 'usuario','etapa']

    # Vista registro
    fieldsets = (
        ('Producto', {
            'fields': ('nombre', 'descripcion','etapa', 'usuario')
        }),
        ('Imagen', {
            'fields': ('fotografia',)
        }),
    )

    # Trucar la descripcion
    def descripcion_truncada(self, obj):
        max_length = 45
        if len(obj.descripcion) > max_length:
            return obj.descripcion[:max_length] + '...'
        else:
            return obj.descripcion

    descripcion_truncada.short_description = 'Descripción'

    def display_fografiaPex(self, obj):
        if obj.fotografia:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.fotografia.url)
        else:
            return 'Sin imagen'

    display_fografiaPex.allow_tags = True
    display_fografiaPex.short_description = 'Producto'
    # TRaer solo los datos de usuario
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(usuario=request.user)
    # Aplicar un selecion
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usuario":
            if request.user.is_superuser:
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)