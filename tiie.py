import requests

# URL base de la API de Banxico para la TIIE
url = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43718/datos/"

# Clave de acceso a la API
apikey = "4a987f27b6d4369993181352f7e6f462ee7a586e979a73756ec6e833799363a1"

# Parámetros de la solicitud HTTP
params = {"token": apikey}

# Enviamos la solicitud HTTP a la API de Banxico
response = requests.get(url, params=params)

# Verificamos que la solicitud se haya realizado correctamente
if response.status_code == 200:
    # Convertimos la respuesta en formato JSON a un diccionario de Python
    data = response.json()
    
    # Obtenemos el último registro de la TIIE
    fecha = data["bmx"]["series"][-1]["datos"][-1]["fecha"]
    tiie = data["bmx"]["series"][-1]["datos"][-1]["dato"]
    
    # Imprimimos el valor de la TIIE
    print("La TIIE más reciente es:", tiie, "a la fecha ", fecha)
else:
    print("Error al obtener la TIIE desde la API de Banxico")