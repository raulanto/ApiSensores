from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html



class CustomAdminSite(admin.AdminSite):
    def register_user_link(self):
        url = reverse('registro')  # Asegúrate de que 'registro' sea el nombre correcto de la URL
        return format_html('<a href="{}">Registrarse</a>', url)

    # Sobrescribe el método get_extra_context para incluir el enlace de registro
    def get_extra_context(self, request):
        extra_context = super().get_extra_context(request)
        extra_context['register_user_link'] = self.register_user_link()
        return extra_context

admin_site = CustomAdminSite(name='myadmin')
