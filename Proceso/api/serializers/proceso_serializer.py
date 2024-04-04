from rest_framework import serializers
from Proceso.models import Proceso
class ProcesoSerializer():
    class Meta:
        model=Proceso
        fields = ['id','descripcion','usuario','equipo']

      # Te odia maldita perralll