from Equipo.actions.actionsEquipo import export_csv
from Equipo.models import SeccionEquipo
from django.contrib import admin

@admin.register(SeccionEquipo)
class SeccionEquipoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','fkequipo','usuario']
    list_filter = ['fkequipo']
    actions = [export_csv]
    def get_queryset(self, request):
        # Obtener el queryset base
        queryset = super().get_queryset(request)

        if request.user.is_superuser:
            # Si el usuario es superusuario, mostrar todas las secciones de equipos
            return queryset
        else:
            # Si el usuario no es superusuario, filtrar las secciones de equipos creadas por este usuario
            return queryset.filter(fkequipo__usuario=request.user)

    def usuario(self, obj):
        # Obtener el usuario asociado al equipo de esta sección
        return obj.fkequipo.usuario.username if obj.fkequipo and obj.fkequipo.usuario else None

    usuario.short_description = 'Usuario'  # Nombre a mostrar en la tabla de admin

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkequipo" and not request.user.is_superuser:
            # Filtrar los equipos disponibles para el usuario actual
            queryset = db_field.related_model.objects.filter(usuario=request.user)
            kwargs["queryset"] = queryset
        return super().formfield_for_foreignkey(db_field, request, **kwargs)