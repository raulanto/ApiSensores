import requests
import time
import random

# URL y token para la API
url = 'http://127.0.0.1:8000/api/v1/lectura/registro/'
token = 'cfc8340bc8d44383934ef380d4a9f71c26305ad6'

# Cabeceras de la petición
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}


# Función para enviar datos de temperatura a la API cada 30 segundos
def enviar_temperatura_cada_30_segundos():
    # Generar un valor inicial de temperatura entre 25 y 35
    temperatura = random.uniform(25, 35)

    while True:
        # Añadir una variación leve a la temperatura (entre -0.5 y 0.5)
        variacion = random.uniform(-0.5, 0.5)
        temperatura += variacion

        # Asegurarse de que la temperatura se mantenga dentro del rango [25, 35]
        if temperatura < 25:
            temperatura = 25
        elif temperatura > 35:
            temperatura = 35

        # Datos que deseas enviar
        data = {
            "valor": round(temperatura, 2),  # Redondeado a 2 decimales
            "fkEtapa": 15,  # Cambia según sea necesario
            "fkESeccionEquipoSensor": 21  # Cambia según sea necesario
        }

        # Enviar los datos a la API
        response = requests.post(url, json=data, headers=headers)

        # Verificar la respuesta
        if response.status_code == 201:
            print(f"Los datos {data} fueron insertados correctamente en la API.")
        else:
            print(f"Hubo un error al insertar los datos {data} en la API:", response.text)

        # Esperar 30 segundos antes de enviar los próximos datos
        time.sleep(30)


# Ejecutar la función
enviar_temperatura_cada_30_segundos()
