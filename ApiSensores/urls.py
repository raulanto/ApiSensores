
'''

APi Sensores
'''



from django.contrib import admin
from django.urls import path,include
from .CustomAuthToken import CustomAuthTokenAPI


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', CustomAuthTokenAPI.as_view()),
    path('api/v1/', include('Plantas.api.urls')),
    path('api/v1/',  include('Producto.api.urls')),
    path('api/v1/', include('Equipo.api.urls')),
    path('api/v1/', include('Proceso.api.urls')),

]
