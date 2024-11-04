from django.contrib import admin
from Proceso.models import Etapa, Proceso
from ..filter.ProcesoFilter import ProcesoFilter

@admin.register(Etapa)
class EtapaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'fkProceso', 'duracion', 'activo','created_at','createdTime_at']
    list_filter = [ProcesoFilter]
    actions = ['frenar_etapas', 'continuar_etapas']
    fieldsets = (
        ('Iniciar Etapa', {
            'fields': ('nombre', 'fkProceso', 'duracion', 'activo')
        }),
    )



    # Devolver solo los queryset del usuario
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(fkProceso__usuario=request.user)

    def formfield_for_foreignkey_proceso(self, db_field, request, **kwargs):
        """
        Personaliza el campo ForeignKey 'organizacion' en el formulario de administración.
        Filtra las organizaciones para mostrar solo las creadas por el usuario actual.
        """
        if db_field.name == "fkProceso":
            kwargs["queryset"] = Proceso.objects.filter(usuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Personaliza los campos ForeignKey en el formulario de administración.
        """
        if db_field.name == "fkProceso":
            return self.formfield_for_foreignkey_proceso(db_field, request, **kwargs)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def frenar_etapas(self, request, queryset):
        for etapa in queryset:
            etapa.frenar(descripcion="Etapa detenida desde el panel de administración.", usuario=request.user)

    frenar_etapas.short_description = "Frenar etapas seleccionadas"

    def continuar_etapas(self, request, queryset):
        for etapa in queryset:
            etapa.continuar(descripcion="Etapa reanudada desde el panel de administración.", usuario=request.user)

    continuar_etapas.short_description = "Continuar etapas seleccionadas"

