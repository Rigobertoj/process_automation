from datetime import datetime
import requests
import dotenv
import os

import requests
config = dotenv.dotenv_values("../env/.env")
TOKEN = config.get("TOKEN_TIIE")
URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos"
def getTiie():
    try:
        #se hace la peticion a la url 
        response = requests.get(URL, headers={"Bmx-Token": TOKEN})
        data = response.json()
        return data
    except requests.HTTPError as httpError:
        print(f"HTTP error {response.status_code}- {httpError}")

    except Exception as error:
        print(error)

    else:
        print("success")

def ultimas_dos_TIIE():
    # obtenemos la data de la API  
    data = getTiie()

    #extreamos los datos de la TIIE
    TIIE = data["bmx"]["series"][0]["datos"]
    #obtenemos su longitud para saber cual es el ultomo dato
    data_len = len(data["bmx"]["series"][0]["datos"])
    ultima_tiie = TIIE[data_len -1]
    penultima_tiie = TIIE[data_len -2 ]
    # print(f"{ultima_tiie} {penultima_tiie}")

    return [ultima_tiie, penultima_tiie]

def fecha(fecha: str | datetime):
    # si fecha no es del tipo string la convertimos en una cade 
    if(type(fecha) != str):
        fecha = str(fecha)
    
    #desempaquetamos el array en 3 variables
    dia, mes, año = fecha.split("/")

    #retornamos los strings 
    return dia, mes, año

    
def TIIE_Actual():
    ultima_tiie, penultima_tiie  = ultimas_dos_TIIE()
    print(ultima_tiie, penultima_tiie)


if __name__ == "__main__":
    ultimas_dos_TIIE()
    # print(TOKEN)