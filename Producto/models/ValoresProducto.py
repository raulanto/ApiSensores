from django.db import models
from .TimeStampedModel import TimeStampedModel
from .Producto import Producto


class ValoresProducto(TimeStampedModel):
    nombre = models.CharField(max_length=50)
    valorMaximo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    valorMinimo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, default=0.0)
    producto = models.ForeignKey(Producto, related_name='producto',on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nombre