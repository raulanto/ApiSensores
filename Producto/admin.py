from django.contrib import admin
from Producto.models import Producto,ValoresProducto
from django.contrib.admin.models import LogEntry,LogEntryManager


# Register your models here.
admin.site.register(Producto)
admin.site.register(ValoresProducto)
admin.site.register(LogEntry)
# admin.site.register(LogEntryManager)