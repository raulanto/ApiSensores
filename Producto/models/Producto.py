from django.db import models
from django.contrib.auth.models import User
from .TimeStampedModel import TimeStampedModel


class Producto(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    etapa=models.CharField(max_length=20,default='Primera Fase')
    fotografia = models.ImageField(blank=True, null=True, default="", upload_to='producto/',verbose_name='ProductoImg')

    def __str__(self):
        return self.nombre