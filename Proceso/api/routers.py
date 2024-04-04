from rest_framework.routers import DefaultRouter, SimpleRouter

from .views.estadoEtapa_view import EstadoEtapaViewSet

router = SimpleRouter()
router.register(r'estadoEtapa', EstadoEtapaViewSet)


