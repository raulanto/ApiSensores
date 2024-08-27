from django.shortcuts import render

from Equipo.models import Equipo, SeccionEquipo


def miprimeravista(request):
    data = {
        'name': "raula antonio",
        'categoria': Equipo.objects.all()
    }

    return render(request, 'index.html', data)


def misegundaavista(request):
    data = {
        'name': "raula antonio",
        'seccionEquipo': SeccionEquipo.objects.all()
    }

    return render(request, 'second.html', data)
