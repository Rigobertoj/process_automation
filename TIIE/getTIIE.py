from datetime import datetime
import requests
import dotenv
import os

import requests
TOKEN = "9692a09b038f044e2980f9895de684d4b6958787fe6ef49ee85d5257005866d1"
URL = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos"
def getTiie():
    try:
        response = requests.get(URL, headers={"Bmx-Token": TOKEN})
        data = response.json()
        return data
    except requests.HTTPError :
        print("HTTP error")

def ultimas_dos_TIIE():
    data = getTiie()
    TIIE = data["bmx"]["series"][0]["datos"]
    data_len = len(data["bmx"]["series"][0]["datos"])
    ultima_tiie = TIIE[data_len -1]
    penultima_tiie = TIIE[data_len -2 ]
    # print(f"{ultima_tiie} {penultima_tiie}")

    return [ultima_tiie, penultima_tiie]

def fecha(fecha: str | datetime):
    if(type(fecha) != datetime):
        fecha = str(fecha)
    
    dia, mes, año = fecha.split("/")
    return año, mes, mes

    
def TIIE_Actual():
    ultima_tiie, penultima_tiie  = ultimas_dos_TIIE()
    print(ultima_tiie, penultima_tiie)


if __name__ == "__main__":
    TIIE_Actual()