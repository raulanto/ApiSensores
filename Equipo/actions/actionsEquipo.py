from django.http import HttpResponse
import csv

def exportequipo_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="equipos.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Planta', 'Usuario'])

    for equipo in queryset:
        writer.writerow([
            equipo.id,
            equipo.nombre,
            equipo.fkplanta.nombre if equipo.fkplanta else '',
            equipo.usuario.username if equipo.usuario else ''
        ])

    return response


exportequipo_csv.short_description = "Descargar CSV"