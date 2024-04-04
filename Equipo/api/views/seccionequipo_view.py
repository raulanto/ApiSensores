from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView
from Equipo.models import SeccionEquipo
from ..serializers.seccionEquipo_serializer import SeccionEquipoSerializer,SeccionEquipoCreateSerializer,SeccionEquipoUpdateSerializer

class SeccionEquipoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = SeccionEquipo.objects.all()

    serializer_class = SeccionEquipoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = SeccionEquipoUpdateSerializer
        return super().update(request, *args, **kwargs)


class SeccionEquipoCreateAPIView(CreateAPIView):
    queryset = SeccionEquipo.objects.all().order_by('id')
    serializer_class = SeccionEquipoCreateSerializer
    permission_classes = [AllowAny]
