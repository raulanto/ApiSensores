
from django.db import models
from django.contrib.auth.models import User
from .TimeStampedModel import TimeStampedModel
class Inconveniente(TimeStampedModel):
    etapa = models.ForeignKey('Etapa', on_delete=models.CASCADE)
    descripcion = models.TextField()
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inconveniente en {self.etapa} - {self.fecha_creacion}"