from django.urls import path
from .views.equipo_views import miprimeravista,misegundaavista


urlpatterns=[
    path('uno',miprimeravista),
    path('dos', misegundaavista)
]