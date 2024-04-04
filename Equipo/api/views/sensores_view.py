from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
from Equipo.models import Sensores
from ..serializers import SensoresSerializer, SensoresCreateSerializer, SensoresUpdateSerializer


class SensoresViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Sensores.objects.all()

    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SensoresUpdateSerializer
        return super().update(request, *args, **kwargs)


class SensoresCreateAPIView(CreateAPIView):
    queryset = Sensores.objects.all().order_by('id')
    serializer_class = SensoresCreateSerializer
    permission_classes = [AllowAny]
