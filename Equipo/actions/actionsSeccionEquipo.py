from django.http import HttpResponse
import csv
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import letter
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="secciones.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Usuario', 'Equipo'])

    for obj in queryset:
        writer.writerow([obj.id, obj.nombre, obj.fkequipo.usuario.username if obj.fkequipo and obj.fkequipo.usuario else None, obj.fkequipo.nombre if obj.fkequipo else None])

    return response

export_csv.short_description = "Exportar como CSV"