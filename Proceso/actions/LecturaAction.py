import csv
from django.http import HttpResponse
import matplotlib.pyplot as plt
from django.db.models import Count
import tempfile


def descargar_valores(self, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="valores_lectura.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Valor', 'Etapa', 'Seccion Equipo Sensor', 'Fecha de Creacion', 'Hora de Creacion'])

    for lectura in queryset:
        writer.writerow([lectura.id, lectura.valor, lectura.fkEtapa, lectura.fkESeccionEquipoSensor, lectura.created_at,
                         lectura.createdTime_at])

    return response


descargar_valores.short_description = "Descargar valores de lectura"


def generar_grafico(self, request, queryset):
    # Obtener el conteo de lecturas por etapa
    lecturas_por_etapa = queryset.values('fkEtapa__nombre').annotate(total=Count('id')).order_by('fkEtapa__nombre')

    # Extraer etiquetas (nombres de las etapas) y valores (conteo de lecturas)
    etiquetas = [lectura['fkEtapa__nombre'] for lectura in lecturas_por_etapa]
    valores = [lectura['total'] for lectura in lecturas_por_etapa]

    # Crear gráfico de líneas
    plt.plot(etiquetas, valores, marker='o')
    plt.xlabel('Etapa')
    plt.ylabel('Cantidad de Lecturas')
    plt.title('Cantidad de Lecturas por Etapa')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Guardar el gráfico en un archivo temporal
    temp_file_path = tempfile.NamedTemporaryFile(suffix='.png').name
    plt.savefig(temp_file_path)

    # Cerrar la figura de Matplotlib para liberar memoria
    plt.close()

    # Devolver la respuesta con el archivo de imagen
    with open(temp_file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='image/png')
        response['Content-Disposition'] = 'attachment; filename="grafico_lecturas.png"'
        return response

generar_grafico.short_description = "Generar gráfico de lecturas por etapa"