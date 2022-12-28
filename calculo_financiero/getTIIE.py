from datetime import datetime
import json
from typing import final
import requests
import dotenv
import os


import requests
config = dotenv.dotenv_values("../env/.env")
TOKEN = config.get("TOKEN_TIIE")
URL = "https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF43783/datos"
def get_series_Tiie() -> json:
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
        print(f"HTTP error {response.status_code} - {httpError}")

    except Exception as error:
        print(error)


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

    return list : una lista de valores de dia : int, mes : int y año : int separados en ese orden
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



def TIIE_Actual() -> dict:
    """
    function que nos permite obtener el valor de la tiee actual atraves de la validacion de las fechas

    return dict : diccionario con claves, fecha : str, dato : int
    """
    #obtenemos las fechas actuales
    fecha_actual = datetime.today()
    año_actual, mes_actual, dia_actual= fecha(fecha_actual)

    #obtemos las ultimas dos TIIE
    ultima_tiie, penultima_tiie  = ultimas_dos_TIIE()

    #desempaquetamos el dia y mes de ambas tiie
    dia_ultima_tiie, mes_ultima_tiie, *_ = fecha(ultima_tiie["fecha"])
    dia_penultima_tiie, mes_penultima_tiie, *_ = fecha(penultima_tiie["fecha"])

    if mes_ultima_tiie <= mes_actual and dia_ultima_tiie <= dia_actual :
        return ultima_tiie

    return penultima_tiie


def convert_datetime(data):
    """convierte obtiene la fecha del objeto data y la transforma de un objeto datatime

    Args:
        data (str): diccionarion con una clave feccha y un avlor en fecha str

    Returns:
        dict: diccionario con el mismo objeto introducido solamente que se cambia el formato de la fecha a datetime
    """
    #obtenemos el valor fecha 
    fecha = data["fecha"]

    #desempaquetamos la fecha y la asignamos a distinras variables
    dia, mes, año = fecha.split("/")
    
    #creamos el tipo datatime 
    fecha_dataTime = datetime.strptime(f"{año}-{mes}-{dia}", '%Y-%m-%d')
    #reasignamos el valor de fecha en el objeto original 
    data["fecha"] = fecha_dataTime
    return data


def TIIE_por_fecha (fecha: str | datetime):
    """funcion que me permite obtener la TIIE mas cercana a la fecha introducida

    Args:
        fecha (str | datetime): fecha con la cual se evaluara y obtendra ell valor mas cercano a la fecha introducida

    Returns:
        dict : diccionario con el la clave fecha  y dato de la TIIE  mas cercana a la fecha introducida
    """

    #retorna el valor de la TIIE en base a una reference de fechas

    #si fecha es del tipo str se convierte a datetime
    if type(fecha) == str:
        dia, mes, año = fecha.split("/")
        print(año)
        fecha = datetime.strptime(f"{año}-{mes}-{dia}", '%Y-%m-%d')
    
    #obtenemos la data de las series
    data = get_series_Tiie()
    
    #obtenemos la data de la TIIE
    TIIE = data["bmx"]["series"][0]["datos"]

    #convertimos las fechas str a datetime
    TIIE_f = list(map(convert_datetime, TIIE))

    #obtenemos las fechas que cumplen la condicion
    value = list(filter(lambda x: x["fecha"] <= fecha, TIIE_f))
    #retornamos el ultimo valor que cumple con la condicion
    return value[-1]

def Tasa_De_Interes_Anual ():
    data = TIIE_Actual()
    TIIE = data["dato"]
    suma_de_interes_profile = 10
    tasa_interes = TIIE + suma_de_interes_profile
    return tasa_interes / 100


if __name__ == "__main__":
    fecha_ = "06/04/2022"
    value = TIIE_por_fecha(fecha_)
    print(value)