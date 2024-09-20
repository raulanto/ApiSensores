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

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Sensores API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="detreaty@gmail.com"),
        license=openapi.License(name="BSD raulanto"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)

urlpatterns = [
                  path('', lambda request: redirect('admin/', permanent=False)),  # Redirige la raíz al admin
                  path('admin/', admin.site.urls),
                  path('api-auth/', include('rest_framework.urls')),
                  path('api-token-auth/', CustomAuthTokenAPI.as_view()),
                  path('api/v1/', include('Plantas.api.urls')),
                  path('api/v1/', include('Producto.api.urls')),
                  path('api/v1/', include('Equipo.api.urls')),
                  path('api/v1/', include('apiS.Proceso.api.urls')),
                  path('registro/', views.registro_usuario, name='registro'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
