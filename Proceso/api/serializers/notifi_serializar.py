from rest_framework import serializers
from Proceso.models import Notificacion

class NotificacionSerializers(serializers.ModelSerializer):
    class Meta:
        model= Notificacion
        fields=['id','user','message','notification_type','created_at','is_read']


class NotificacionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model= Notificacion
        fields=['user','message','notification_type']


class NotificacionUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model= Notificacion
        fields=['is_read']