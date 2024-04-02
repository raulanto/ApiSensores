from django.urls import path
from .routers import router
from .views import PlantaCreateAPIView

urlpatterns = [
    path('planta/registro/', PlantaCreateAPIView.as_view(), name='plantaRegistro'),
]

urlpatterns += router.urls
