from rest_framework.routers import DefaultRouter, SimpleRouter

from .views.estadoEtapa_view import EstadoEtapaViewSet
from .views.proceso_view import ProcesoViewSet
from .views.etapa_view import EtapaViewSet
router = SimpleRouter()
router.register(r'estadoEtapa', EstadoEtapaViewSet)
router.register(r'proceso', ProcesoViewSet)
router.register(r'etapa',EtapaViewSet)
