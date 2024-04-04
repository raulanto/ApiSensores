from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Equipo.api.serializers.equiupo_serializer import EquipoSerializer, EquipoCreateSerializer, EquipoUpdateSerializer
from Equipo.models import Equipo


class EquipoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = Equipo.objects.all()

    serializer_class = EquipoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = EquipoUpdateSerializer
        return super().update(request, *args, **kwargs)


class EquipoCreateAPIView(CreateAPIView):
    queryset = Equipo.objects.all().order_by('id')
    serializer_class = EquipoCreateSerializer
    permission_classes = [AllowAny]
