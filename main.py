import requests

# Datos que deseas insertar en la API
data = [
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.90, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.80, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.7, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.1, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.9, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.8, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.00, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 6.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.3, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.2, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.3, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.7, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.3, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.3, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.4, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.5, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3},
  {"valor": 5.6, "fkEtapa": 4, "fkESeccionEquipoSensor": 3}
]


# URL de tu API donde quieres insertar los datos
url = 'http://127.0.0.1:8000/api/v1/lectura/registro/'

# Token de autenticación
token = '4dc372c750cfa0aab10d0df78bdd816ac9fcebb7'

# Encabezados de la solicitud con el token de autenticación
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}

# Realizar la solicitud POST a la API
response = requests.post(url, json=data, headers=headers)

# Realizar solicitudes POST individuales para cada objeto de datos
for item in data:
    response = requests.post(url, json=item, headers=headers)
    if response.status_code == 201:
        print(f"Los datos {item} fueron insertados correctamente en la API.")
    else:
        print(f"Hubo un error al insertar los datos {item} en la API:", response.text)