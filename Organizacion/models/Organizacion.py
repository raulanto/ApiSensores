from django.db import models
from django.contrib.auth.models import User
from .TimeStampedModel import TimeStampedModel

# Numero de telefono
from phonenumber_field.modelfields import PhoneNumberField


class Organizacion(TimeStampedModel):
    # Datos de la organizacion
    nombre = models.CharField(max_length=45, default='Organizacion')
    fkUsuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Usuario')
    descripcion = models.TextField(max_length=250, default='Empresa de Acuicultura ')
    # Datos adicionales
    con_Telefono = PhoneNumberField(blank=True, null=True,verbose_name='Telefono',default='9999999')
    con_email=models.EmailField(verbose_name="Correo",blank=True, null=True)

    matricula = models.CharField(max_length=8, default='afw3fdfs')

    logo = models.ImageField(blank='', default="", upload_to='logo/')

    def __str__(self):
        return self.nombre
