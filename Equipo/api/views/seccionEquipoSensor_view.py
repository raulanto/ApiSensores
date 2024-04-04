from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
from Equipo.models import SeccionEquipoSensor
from ..serializers.seccionEquipoSensor_serializer import SeccionEquipoSensorSerializer, \
    SeccionEquipoSensorCreateSerializer, SeccionEquipoSensorUpdateSerializer


class SeccionEquipoSemsorViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = SeccionEquipoSensor.objects.all()

    serializer_class = SeccionEquipoSensorSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SeccionEquipoSensorUpdateSerializer
        return super().update(request, *args, **kwargs)


class SeccionEquipoSensorCreateAPIView(CreateAPIView):
    queryset = SeccionEquipoSensor.objects.all().order_by('id')
    serializer_class = SeccionEquipoSensorCreateSerializer
    permission_classes = [AllowAny]
