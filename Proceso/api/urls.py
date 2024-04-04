from django.urls import path
from .routers import router
from .views.estadoEtapa_view import EstadoEtapaProductoCreateViewSet

urlpatterns = [
    path('estadoEtapa/registro/', EstadoEtapaProductoCreateViewSet.as_view(), name='estadoEtapa'),

]

urlpatterns += router.urls
