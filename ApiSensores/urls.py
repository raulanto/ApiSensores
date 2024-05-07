'''

APi Sensores
'''

from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from .CustomAuthToken import CustomAuthTokenAPI
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', lambda request: redirect('admin/', permanent=False)),  # Redirige la raíz al admin
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthTokenAPI.as_view()),
    path('api/v1/', include('Plantas.api.urls')),
    path('api/v1/', include('Producto.api.urls')),
    path('api/v1/', include('Equipo.api.urls')),
    path('api/v1/', include('Proceso.api.urls')),
    path('registro/', views.registro_usuario, name='registro'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
