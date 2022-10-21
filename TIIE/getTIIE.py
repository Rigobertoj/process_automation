from datetime import datetime
import requests
import dotenv
import os

import requests
config = dotenv.dotenv_values("../env/.env")
TOKEN = config.get("TOKEN_TIIE")
URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos"
def get_series_Tiie():
    """
    obtemos todos los datos de la API de banxico, sobre los valores de la TIIE 
    
    return json : este tiene los datos de la API de banxico 
    """
    
    try:
        #se hace la peticion a la url 
        response = requests.get(URL, headers={"Bmx-Token": TOKEN})
        data = response.json()
    except requests.HTTPError as httpError:
        #si da algun valor https se imprime por pantalla 
        print(f"HTTP error {response.status_code}- {httpError}")

    except Exception as error:
        print(error)

    else:
        print("success")

    return data
    

def ultimas_dos_TIIE() -> list:
    """
    obtenemos los dos ultimos datos de la peticion TIIE a la fehca actula,  \n
    estos estan en un diccionario cada uno con clave fecha, dato,

    return list : lista con los valores de la ultima y penultima tiie
    """

    # obtenemos la data de la API  
    data = get_series_Tiie()

    #extreamos los datos de la TIIE
    TIIE = data["bmx"]["series"][0]["datos"]

    #extraemos los dos ultimos datos 
    ultima_tiie = TIIE.pop()
    penultima_tiie = TIIE.pop()

    return [ultima_tiie, penultima_tiie]

def fecha(fecha: str | datetime) -> list[str, str, str]:
    """
    descopone la fecha introducida en dia, mes y año

    param fecha : fecha la cual se quiere descoponer
    
    return list : una lista de valores de dia, mes y año separados en ese orden
    """

    # si fecha no es del tipo string la convertimos en una cade 
    if(type(fecha) != str):
        fecha = str(fecha)

    
    if " " in fecha:
        #si tiene timepo y fecha esta se dividen
        fecha = fecha.split(" ")
        #asignamos la parte de la fecha 
        fecha = fecha[0]

    #si esta separada por - las seperamos por -
    if "-" in fecha:
        dia, mes, año, *resto = fecha.split("-")
        dia =int(dia)
        mes = int(mes)
        año = int(año)
        return [dia, mes, año]

    #si esta separada por / las seperamos por /   
    if "/" in fecha:
        dia, mes, año, *resto = fecha.split("/")
        dia =int(dia)
        mes = int(mes)
        año = int(año)
        return [dia, mes, año]


    
def TIIE_Actual():
    #obtenemos las fechas actuales
    dia_actual = datetime.today()
    dia_actual, mes_actual, *_ = fecha(dia_actual)

    #obtemos las ultimas dos TIIE
    ultima_tiie, penultima_tiie  = ultimas_dos_TIIE()
    
    #desempaquetamos el dia y mes de ambas tiie
    dia_ultima_tiie, mes_ultima_tiie, *_ = fecha(ultima_tiie["fecha"])
    dia_penultima_tiie, mes_penultima_tiie, *_ = fecha(penultima_tiie["fecha"])

    if mes_penultima_tiie <= mes_actual & dia_ultima_tiie <= dia_actual :
        return ultima_tiie

    return penultima_tiie
    




if __name__ == "__main__":
    value = TIIE_Actual()
    print(value)
    # print(TOKEN)