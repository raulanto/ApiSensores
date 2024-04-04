from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import EquipoViewSet,SeccionEquipoViewSet,SensoresViewSet,SeccionEquipoSemsorViewSet

router = SimpleRouter()
router.register(r'equipo', EquipoViewSet)
router.register(r'seccionEquipo', SeccionEquipoViewSet)
router.register(r'sensor', SensoresViewSet)
router.register(r'seccionSensor',SeccionEquipoSemsorViewSet)