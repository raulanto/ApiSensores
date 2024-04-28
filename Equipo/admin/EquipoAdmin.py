
from Equipo.models import Equipo

from django.contrib import admin



@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'fkplanta', 'usuario']
    list_display_links = ['id', 'nombre']
    list_filter = ['fkplanta']
    list_per_page = 10

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        # Filtrar los equipos por el usuario
        if request.user.is_superuser:
            # Si el usuario es un superusuario, mostrar todos los equipos
            return queryset
        else:
            # Si el usuario no es superusuario, filtrar los equipos creados por este usuario
            return queryset.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        # Asignar el usuario actual como creador del equipo al guardarlo
        if not change:  # Solo si es un nuevo objeto
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkplanta":
            # Filtrar las plantas por el usuario actual si no es superusuario
            if not request.user.is_superuser:
                kwargs["queryset"] = db_field.related_model.objects.filter(usuario=request.user)
        elif db_field.name == "usuario":
            if request.user.is_superuser:
                # Permitir la modificación del campo para superusuarios
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                # Establecer el usuario actual y deshabilitar el campo para otros usuarios
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
