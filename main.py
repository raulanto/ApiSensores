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

# Función para enviar datos a la API cada 30 segundos
def enviar_datos_cada_30_segundos():
    # Generar un valor inicial entre 5 y 7
    valor = random.uniform(5, 7)

    while True:
        # Añadir una variación leve al valor (entre -0.1 y 0.1)
        variacion = random.uniform(-0.1, 0.1)
        valor += variacion

        # Asegurarse de que el valor se mantenga dentro del rango [5, 7]
        if valor < 5:
            valor = 5
        elif valor > 7:
            valor = 7

        # Datos que deseas enviar
        data = {
            "valor": round(valor, 2),  # Redondeado a 2 decimales
            "fkEtapa": 15,  # Cambia según sea necesario
            "fkESeccionEquipoSensor": 20  # Cambia según sea necesario
        }

        # Enviar los datos a la API
        response = requests.post(url, json=data, headers=headers)

        # Verificar la respuesta
        if response.status_code == 201:
            print(f"Los datos {data} fueron insertados correctamente en la API.")
        else:
            print(f"Hubo un error al insertar los datos {data} en la API:", response.text)

        # Esperar 30 segundos antes de enviar los próximos datos
        time.sleep(5)

# Ejecutar la función
enviar_datos_cada_30_segundos()
