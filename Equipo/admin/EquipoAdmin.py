from Equipo.actions.actionsEquipo import exportequipo_csv
from Equipo.models import Equipo

from django.contrib import admin

# Clase filtrado especial
from Plantas.filter.Plantafilter import PlantaFilter
@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    # Vista tabla
    list_display = ['id', 'nombre', 'nombre_planta', 'usuario', 'fkproducto','fkplanta']
    list_display_links = ['id', 'nombre']
    list_filter = [PlantaFilter]
    list_per_page = 10
    actions = [exportequipo_csv]
    # VistaRegistro
    fieldsets = (
        ('Datos Equipo', {
            'fields': ('nombre', 'descripcion', 'fkplanta', 'usuario')
        }),
        ('Producto', {
            'fields': ('fkproducto',)
        }),
    )

    def nombre_planta(self, obj):
        return obj.fkplanta.nombre

    nombre_planta.short_description = 'Planta'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # Filtrar los equipos
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        # Asignar el usuario actual
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkplanta":
            # Filtrar las plantas
            if not request.user.is_superuser:
                kwargs["queryset"] = db_field.related_model.objects.filter(usuario=request.user)
        elif db_field.name == "usuario":
            if request.user.is_superuser:
                # Permitir la modificación
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                # usuario actual y deshabilitar
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        elif db_field.name == "fkproducto":
            # productos por el usuario
            if not request.user.is_superuser:
                kwargs["queryset"] = db_field.related_model.objects.filter(usuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

