# lectura etapa view

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin
)

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from ..serializers.lecturaEtapa_serializer import LecturaEtapaSerializer,LecturaEtapaCreateSerializer
from Proceso.models.LecturaEtapa import LecturaEtapa
# Cabios de registros impor
from ApiSensores.registroCambios import registrarCambio

# filtros
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class LecturaEtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet
):
    queryset = LecturaEtapa.objects.all()
    serializer_class = LecturaEtapaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['fkESeccionEquipoSensor', 'valor', 'fkEtapa']
    search_fields = ['valor', 'fkEtapa']

    @action(detail=False, methods=['get'], url_path='last')
    def get_last_lectura(self, request):
        # Obtén los parámetros de filtrado desde los query params
        fkESeccionEquipoSensor = request.query_params.get('fkESeccionEquipoSensor')
        fkEtapa = request.query_params.get('fkEtapa')

        # Filtro basado en los campos proporcionados
        if fkESeccionEquipoSensor and fkEtapa:
            # Filtra por los campos dados y ordena por el último registro según algún campo, como 'created_at'
            try:
                last_lectura = LecturaEtapa.objects.filter(
                    fkESeccionEquipoSensor=fkESeccionEquipoSensor,
                    fkEtapa=fkEtapa
                ).latest('createdTime_at')  # Usa el campo que defina el orden cronológico

                serializer = self.get_serializer(last_lectura)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except LecturaEtapa.DoesNotExist:
                return Response(
                    {'detail': 'No se encontró ninguna lectura para los filtros dados.'},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {'detail': 'Los parámetros fkESeccionEquipoSensor y fkEtapa son requeridos.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class LecturaEtapaCreateViewSet(CreateAPIView):
    queryset = LecturaEtapa.objects.all()
    serializer_class = LecturaEtapaCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()

        # Registra el cambio
        mensaje = "Lectura creado"
        registrarCambio(self.request, instance, mensaje)