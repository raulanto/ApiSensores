# Cabios de registros impor
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.contenttypes.models import ContentType
from django.utils.encoding import force_str


def registrarCambio(request, objeto, mensaje):
    LogEntry.objects.create(
        user_id=request.user.id,
        content_type_id=ContentType.objects.get_for_model(objeto).pk,
        object_id=objeto.pk,
        object_repr=force_str(objeto),
        action_flag=CHANGE,
        change_message=mensaje,
    )