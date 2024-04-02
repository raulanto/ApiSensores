from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Plantas.api.serializers import PlantaSerializer,PlantaCreateSerializer,PlantaUpdateSerializer
from Plantas.models import *

class PlantaViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Planta.objects.all()

    serializer_class = PlantaSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = PlantaUpdateSerializer
        return super().update(request, *args, **kwargs)


class PlantaCreateAPIView(CreateAPIView):
    queryset = Planta.objects.all().order_by('id')
    serializer_class = PlantaCreateSerializer
    permission_classes = [AllowAny]