from django.contrib import admin

from Organizacion.models import Organizacion

from django.utils.html import format_html


# Register your models here.

@admin.register(Organizacion)
class AdminOrganizacion(admin.ModelAdmin):
    list_display = ['id', 'display_logo', 'nombre', 'descripcion', 'fkUsuario', 'con_Telefono', 'con_email']
    list_editable = ['nombre']
    search_fields = ['nombre']

    # Vista registro
    fieldsets = (
        ('Datos Organizacion', {
            'fields': ('nombre', 'descripcion', 'fkUsuario')
        }),
        ('Matricula', {
            'fields': ('matricula',)
        }),
        ('Logo', {
            'fields': ('logo',)
        }),
        ('Contacto', {
            'fields': ('con_Telefono', 'con_email')
        }),
    )

    def display_logo(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.logo.url)
        else:
            return 'Sin Logo'

    display_logo.allow_tags = True
    display_logo.short_description = 'Logo'

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(fkUsuario=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkUsuario":
            if request.user.is_superuser:
                return super().formfield_for_foreignkey(db_field, request, **kwargs)
            else:
                kwargs["initial"] = request.user.id
                kwargs["disabled"] = True
        return super().formfield_for_foreignkey(db_field, request, **kwargs)