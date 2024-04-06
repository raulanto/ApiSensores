from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords # new line
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Producto(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    history = HistoricalRecords()
    def __str__(self):
        return self.nombre

class ValoresProducto(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    valorMaximo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    valorMinimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    producto = models.ForeignKey(Producto, related_name='producto',on_delete=models.CASCADE, blank=True, null=True)


    history = HistoricalRecords()

    def __str__(self):
        return self.nombre