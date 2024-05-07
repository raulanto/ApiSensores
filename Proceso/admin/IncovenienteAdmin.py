from ..models.Inconveniente import Inconveniente

from django.contrib import admin


@admin.register(Inconveniente)
class InconvenienteAdmin(admin.ModelAdmin):
    pass