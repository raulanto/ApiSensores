from django.urls import path
from .routers import router
from .views import EquipoCreateAPIView, SeccionEquipoCreateAPIView, SensoresCreateAPIView, \
    SeccionEquipoSensorCreateAPIView, EquipoHistoryViewSet

urlpatterns = [
    path('equipo/registro/', EquipoCreateAPIView.as_view(), name='plantaEquipo'),
    path('seccionEquipo/registro/', SeccionEquipoCreateAPIView.as_view(), name='aseccionEquipo'),
    path('sensor/registro/', SensoresCreateAPIView.as_view(), name='sensor'),
    path('seccionSensor/registro/', SeccionEquipoSensorCreateAPIView.as_view(), name='seccionSensor'),
    path('equipo/<int:pk>/historial/', EquipoHistoryViewSet.as_view({'get': 'list'}), name='equipo-historial'),
]

urlpatterns += router.urls
