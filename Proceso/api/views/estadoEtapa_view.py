from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView




from ..serializers import EstadoEtapaSerializer,EstadoEtapaCreateSerializer,EstadoEtapaUpdateSerializer

from Proceso.models import EstadoEtapa


class EstadoEtapaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = EstadoEtapa.objects.all()

    serializer_class = EstadoEtapaSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = EstadoEtapaUpdateSerializer
        return super().update(request, *args, **kwargs)


class EstadoEtapaProductoCreateViewSet(CreateAPIView):
    queryset = EstadoEtapa.objects.all()
    serializer_class = EstadoEtapaCreateSerializer
    permission_classes = [AllowAny]