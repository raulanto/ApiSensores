from django.contrib import admin
from ..models import Planta, Municipio, Estado


@admin.register(Planta)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'usuario', 'municipio', 'organizacion']
    list_display_links = ['id', 'nombre']
    list_filter = ['organizacion']
    list_per_page = 10

    # # excluir los datos a modificar
    # exclude = ['usuario']

    # VistaRegistro
    fieldsets = (
        ('Datos Planta', {
            'fields': ('nombre', 'descripcion','usuario','organizacion')
        }),
        ('Ubicacion', {
            'fields': ('calle', 'codigo_postal', 'municipio')
        }),
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            # Si el usuario es superadmin, mostrar todas las plantas
            return queryset
        else:
            # Filtrar las plantas por el usuario actual
            return queryset.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        # Asignar el usuario actual como creador de la planta al guardarla
        if not change:  # Solo si es un nuevo objeto
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def get_exclude(self, request, obj=None):
        # Si el usuario es superadmin, no se excluye el campo de usuario
        if request.user.is_superuser:
            return []
        else:
            # Si no es superadmin, se excluye el campo de usuario para evitar modificaciones
            return ['usuario']
