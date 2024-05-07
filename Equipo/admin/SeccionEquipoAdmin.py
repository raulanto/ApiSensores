from Equipo.actions.actionsSeccionEquipo import exportSeccionEquipo_csv
from Equipo.models import SeccionEquipo
from django.contrib import admin

from ..filter.EquipoFilter import EquipoFilter
@admin.register(SeccionEquipo)
class SeccionEquipoAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','nombre_equipo','usuario']
    list_filter = [EquipoFilter]
    actions = [exportSeccionEquipo_csv]

    def nombre_equipo(self, obj):
        return obj.fkequipo.nombre

    nombre_equipo.short_description = 'Equipo'
    def get_queryset(self, request):

        queryset = super().get_queryset(request)

        if request.user.is_superuser:

            return queryset
        else:

            return queryset.filter(fkequipo__usuario=request.user)

    def usuario(self, obj):

        return obj.fkequipo.usuario.username if obj.fkequipo and obj.fkequipo.usuario else None

    usuario.short_description = 'Usuario'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "fkequipo" and not request.user.is_superuser:

            queryset = db_field.related_model.objects.filter(usuario=request.user)
            kwargs["queryset"] = queryset
        return super().formfield_for_foreignkey(db_field, request, **kwargs)