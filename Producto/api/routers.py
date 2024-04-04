from rest_framework.routers import DefaultRouter, SimpleRouter

from Producto.api.views import ValoresProductoViewSet,ProductoViewSet

router = SimpleRouter()
router.register(r'valoresproducto', ValoresProductoViewSet)
router.register(r'producto',ProductoViewSet)


