import csv

from django.http import HttpResponse


def exportSeccionequipoSensor_csv(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="secciones_equipos_sensores.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Sección del Equipo', 'Sensor', 'Equipo'])

    for seccion_equipo_sensor in queryset:
        writer.writerow([
            seccion_equipo_sensor.id,
            seccion_equipo_sensor.fkseccionEquipo.nombre if seccion_equipo_sensor.fkseccionEquipo else '',
            seccion_equipo_sensor.fksensor.nombre if seccion_equipo_sensor.fksensor else '',
            seccion_equipo_sensor.fkseccionEquipo.fkequipo.nombre if seccion_equipo_sensor.fkseccionEquipo else ''
        ])

    return response


exportSeccionequipoSensor_csv.short_description = "Descargar CSV"