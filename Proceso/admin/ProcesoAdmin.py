from django.contrib import admin
from Proceso.models.Proceso import Proceso


@admin.register(Proceso)
class ProcesoAdmin(admin.ModelAdmin):
    pass