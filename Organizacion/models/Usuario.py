from django.db import models
from django.contrib.auth.models import User
from .Organizacion import Organizacion
from .TimeStampedModel import TimeStampedModel
class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE, related_name='usuariosOrg', blank=True, null=True)

    def __str__(self):
        return self.user.username