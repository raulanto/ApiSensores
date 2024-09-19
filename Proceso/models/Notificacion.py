from django.db import models
from django.contrib.auth.models import User

from Proceso.models import TimeStampedModel

class Notificacion(TimeStampedModel):
    NOTIFICATION_TYPES = (
        ('info', 'Informacion'),
        ('warning', 'Problema'),
        ('error', 'Error'),
        ('success', 'Exito'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    tittle =models.CharField(max_length=50,default='Esto es un titulo')
    message = models.TextField() 
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES, default='info')
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def __str__(self):
        return f'{self.user.username} - {self.notification_type} - {self.message[:20]}'

    class Meta:
        ordering = ['-created_at']