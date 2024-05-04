# AdminSensores
 
## Al clonar el repositorio el primer paso que se tiene que hacer es crear el entorno virtual

### Verificar que estés en tu rama

Para verificar que estás en tu rama en Git, puedes utilizar el siguiente comando en tu terminal:

```bash
git branch
````
Crear un entorno virtual con `virtualenv` es un proceso sencillo y útil para gestionar las dependencias de un proyecto de Python. Aquí te doy los pasos básicos para crear y activar un entorno virtual:

1. **Instala `virtualenv` (si aún no lo has hecho):**
    
    Puedes instalar `virtualenv` utilizando `pip`, el gestor de paquetes de Python. Abre tu terminal y ejecuta el siguiente comando:
    
    bash
    

```
pip install virtualenv
```
    
- **Crea un entorno virtual:**
    
    Navega hasta el directorio de tu proyecto en la terminal y ejecuta el siguiente comando para crear un entorno virtual. Puedes reemplazar `nombre_del_entorno` con el nombre que desees para tu entorno virtual:
    
    bash
```
virtualenv nombre_del_entorno
```

    
Esto creará un directorio con el nombre que hayas especificado, conteniendo la estructura del entorno virtual.
    
- **Activa el entorno virtual:**
    
    El proceso para activar el entorno virtual depende del sistema operativo:
    
    - **En Windows:**
        
        bash
```
.\nombre_del_entorno\Scripts\activate
```
    
    
Después de ejecutar este comando, verás el nombre de tu entorno virtual en el prompt, indicando que el entorno está activo.
    
- **Desactivar el entorno virtual:**
    
    Para desactivar el entorno virtual y volver al entorno global de Python, simplemente ejecuta:
    
    bash
    

```bash
deactivate
```

### Instalcion de requerimientos 

El comando ``pip install -r requirements.txt`` se utiliza para instalar todos los requrimientos que estan en el proyecto

# Depues de instalar los requerimientos viene la parte de migraciones

- **Aplicar migraciones iniciales:**
    
    Antes de ejecutar el servidor de desarrollo, realiza las migraciones iniciales para configurar la base de datos. Ejecuta el siguiente comando:
    
    bash
    
```
python manage.py makemigrations Catalagos
python manage.py migrate
```
en este caso es  se hace con el ejemplo de catalagos es decir el modulo en cual estes trabajando se haran las makemigrations
- **Crear un superusuario (opcional):**
    
    Si deseas crear un superusuario para administrar la interfaz de administración de Django, utiliza el siguiente comando y sigue las instrucciones:
    
    bash
    
```
python manage.py createsuperuser
```
    
- **Ejecutar el servidor de desarrollo:**
    
    Finalmente, puedes iniciar el servidor de desarrollo con el siguiente comando:
    
    bash
    

```bash
python manage.py runserver
```
