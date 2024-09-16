from rest_framework.routers import DefaultRouter, SimpleRouter

from .views.estadoEtapa_view import EstadoEtapaViewSet
from .views.proceso_view import ProcesoViewSet
from .views.etapa_view import EtapaViewSet
from .views.lecturaEtapa_view import LecturaEtapaViewSet
from .views.notifi_view import NotificacionViewSet
router = SimpleRouter()
router.register(r'estadoEtapa', EstadoEtapaViewSet)
router.register(r'proceso', ProcesoViewSet)
router.register(r'etapa',EtapaViewSet)
router.register(r'lectura',LecturaEtapaViewSet)
router.register(r'notificacion',NotificacionViewSet)