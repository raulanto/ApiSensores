from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
)
from rest_framework.generics import CreateAPIView

from Producto.models import ValoresProducto

from ..serializers import ValoresProductoCreateSerializer ,ValoresProductoUpdateSerializer,ValoresProductoSerializer

class ValoresProductoViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
    GenericViewSet
):
    queryset = ValoresProducto.objects.all()

    serializer_class = ValoresProductoSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        self.serializer_class = ValoresProductoUpdateSerializer
        return super().update(request, *args, **kwargs)


class ValoresProductoCreateViewSet(CreateAPIView):
    queryset = ValoresProducto.objects.all()
    serializer_class = ValoresProductoCreateSerializer
    permission_classes = [AllowAny]