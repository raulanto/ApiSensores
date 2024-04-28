from django.contrib import admin

from Equipo.models import Sensores


@admin.register(Sensores)
class SensoresAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'usuario', 'matricula']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            # Si el usuario es superusuario, mostrar todos los sensores
            return queryset
        else:
            # Si el usuario no es superusuario, filtrar los sensores por el usuario actual
            return queryset.filter(usuario=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "usuario":
            if request.user.is_superuser:
                # Permitir la modificación del campo para superusuarios
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                # Establecer el usuario actual y deshabilitar el campo para otros usuarios
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)