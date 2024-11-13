# project_settings.py
from pathlib import Path
import os
# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Clave secreta y debug
SECRET_KEY = 'django-insecure-t9j*^2jv_^om$ru!+wz+zq^851cn!xqvk01itibc#*=fe-dufp'

DEBUG = True



# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'u889902058_apisensores',
    #     'USER': 'u889902058_admin',
    #     'PASSWORD': 'rraa18uL52.',
    #     'HOST': '154.56.47.204',  # Si tu MySQL está en un servidor diferente, cambia esto.
    #     'PORT': '3306',  # Puerto predeterminado de MySQL.
    # }
}
# Archivos estáticos
STATIC_URL = 'static/'

# defino la url para que mande al admin
LOGIN_REDIRECT_URL = '/admin/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
