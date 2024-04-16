from rest_framework.serializers import ModelSerializer
from Organizacion.models import Organizacion

class OrganizacionSerializer(ModelSerializer):
    class Meta:
        model=Organizacion
        fileds=['id','nombre','fkUsuario','descripcion']


class OrganizacionCreateSerializer(ModelSerializer):
    class Meta:
        model=Organizacion
        fileds=['nombre','fkUsuario','descripcion']