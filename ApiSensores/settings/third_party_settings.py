# third_party_settings.py
from .django_settings import *

THIRD_PARTY_APPS = [
    'import_export',
    'coreapi',
    'rest_framework',
    'rest_framework.authtoken',
    'simple_history',
    'django_filters',
    'corsheaders',

]

LOCAL_APPS = [
    'Plantas.apps.PlantasConfig',
    'Producto.apps.ProductoConfig',
    'Equipo.apps.EquipoConfig',
    'Proceso.apps.ProcesoConfig',
    'Organizacion.apps.OrganizacionConfig'
]

# defino la url para que mande al admin
LOGIN_REDIRECT_URL = '/admin/'

INSTALLED_APPS += THIRD_PARTY_APPS + LOCAL_APPS


# Configuración específica para aplicaciones de terceros
CORS_ALLOW_ALL_ORIGINS = True

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',

    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5000,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
}
