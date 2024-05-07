from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect



def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/')  # Redirige al panel de administración
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


