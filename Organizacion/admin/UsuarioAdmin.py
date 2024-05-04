from django.contrib import admin

from Organizacion.models import Usuario,Organizacion


@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    list_display = ['id','user','organizacion']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "organizacion":
            if request.user.is_superuser:
                # Si es superusuario, mostrar todas las organizaciones
                kwargs["queryset"] = Organizacion.objects.all()
            else:
                # Filtrar las organizaciones por el usuario actual
                kwargs["queryset"] = Organizacion.objects.filter(fkUsuario=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)