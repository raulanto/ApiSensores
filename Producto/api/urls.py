from django.urls import path
from .routers import router
from .views import ValoresProductoCreateViewSet ,ProductoCreateViewSet

urlpatterns = [
    path('valoresproducto/registro/', ValoresProductoCreateViewSet.as_view(), name='valoresproductoRegistro'),
    path('producto/registro/', ProductoCreateViewSet.as_view(), name='productoRegistro'),
]

urlpatterns += router.urls
