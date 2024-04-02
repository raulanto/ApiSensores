from django.contrib import admin
from .models import Planta,Municipio,Estado
# Register your models here.


admin.site.register(Municipio)
admin.site.register(Estado)


@admin.register(Planta)
class PlantasAdmin(admin.ModelAdmin):
    list_display = ['nombre','usuario']