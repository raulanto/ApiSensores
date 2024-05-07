from django.contrib import admin
from ..models import Planta
from Organizacion.models.Organizacion import Organizacion
from Organizacion.filters.OrganizacionFilter import OrganizacionFilter


@admin.register(Planta)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'municipio', 'organizacion','usuario']
    list_display_links = ['id']
    list_per_page = 10
    list_filter = [OrganizacionFilter]

    # VistaRegistro
    fieldsets = (
        ('Datos Planta', {
            'fields': ('nombre', 'descripcion','organizacion','usuario')
        }),
        ('Ubicacion', {
            'fields': ('calle', 'codigo_postal', 'municipio')
        }),
    )

    # Devolver solo los queryset del usuario
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:

            return queryset
        else:

            return queryset.filter(usuario=request.user)

    def save_model(self, request, obj, form, change):
        """
        Asigna el usuario actual como el usuario de la planta
        """
        if not obj.usuario_id:  # Si el usuario no ha sido asignado
            obj.usuario = request.user
        super().save_model(request, obj, form, change)

    def formfield_for_foreignkey_usuario(self, db_field, request, **kwargs):
        """
        Personaliza el campo ForeignKey 'usuario' en el formulario de administración.
        """
        if db_field.name == "usuario":
            if request.user.is_superuser:
                # Permitir la modificación del campo para superusuarios
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                # Establecer el usuario actual como valor inicial y deshabilitar el campo para otros usuarios
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_foreignkey_organizacion(self, db_field, request, **kwargs):
        """
        Personaliza el campo ForeignKey 'organizacion' en el formulario de administración.
        Filtra las organizaciones para mostrar solo las creadas por el usuario actual.
        """
        if db_field.name == "organizacion":
            # Filtrar las organizaciones para mostrar solo las creadas por el usuario actual
            kwargs["queryset"] = Organizacion.objects.filter(fkUsuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Personaliza los campos ForeignKey en el formulario de administración.
        """
        if db_field.name == "usuario":
            return self.formfield_for_foreignkey_usuario(db_field, request, **kwargs)
        elif db_field.name == "organizacion":
            return self.formfield_for_foreignkey_organizacion(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


