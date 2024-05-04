from django.urls import path
from .views.UserRegistro import register

urlpatterns = [
    # Otras URL aquí...
    path('registro/', register, name='registro'),
]
