from rest_framework.routers import DefaultRouter, SimpleRouter

from Plantas.api.views import PlantaViewSet

router = SimpleRouter()
router.register(r'planta', PlantaViewSet)


