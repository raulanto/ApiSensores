from django.urls import path
from .routers import router
from .views.estadoEtapa_view import EstadoEtapaProductoCreateViewSet
from .views.proceso_view import ProcesoCreateViewSet
from .views.etapa_view import EtapaCreateViewSet
from .views.lecturaEtapa_view import LecturaEtapaCreateViewSet
urlpatterns = [
    path('estadoEtapa/registro/', EstadoEtapaProductoCreateViewSet.as_view(), name='estadoEtapa'),
    path('proceso/registro/', ProcesoCreateViewSet.as_view(), name='proceso'),
    path('etapa/registro/', EtapaCreateViewSet.as_view(), name='etapa'),
    path('lectura/registro/', LecturaEtapaCreateViewSet.as_view(), name='lectura'),

]

urlpatterns += router.urls
