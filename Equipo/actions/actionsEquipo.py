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

# def export_pdf(modeladmin, request, queryset):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="secciones.pdf"'
#
#     doc = SimpleDocTemplate(response, pagesize=letter)
#     table_data = [['ID', 'Nombre', 'Usuario', 'Equipo']]
#
#     for obj in queryset:
#         table_data.append([obj.id, obj.nombre, obj.fkequipo.usuario.username if obj.fkequipo and obj.fkequipo.usuario else None, obj.fkequipo.nombre if obj.fkequipo else None])
#
#     table = Table(table_data)
#     style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
#                         ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
#                         ('ALIGN', (0,0), (-1,-1), 'CENTER'),
#                         ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
#                         ('BOTTOMPADDING', (0,0), (-1,0), 12),
#                         ('BACKGROUND', (0,1), (-1,-1), colors.beige),
#                         ('GRID', (0,0), (-1,-1), 1, colors.black)])
#
#     table.setStyle(style)
#     doc.build([table])
#     return response
#
# export_pdf.short_description = "Exportar como PDF"
