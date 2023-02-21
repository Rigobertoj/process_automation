import copy as c
from functools import reduce


def sort_dict_by_value(d : dict[str : int | float]) -> dict: 
    """
    Descripcion : funcion que nos permite ordenar un diccionario en vase a su valor

    Params:
        - d (dict) : diccionario 
    
    return (dict) : retorna el mismo diccionario ordenao en base a su valores
    """
    return dict(sorted(d.items(), key=lambda item: item[1]))


def reduce_two_list_dict(dict: dict, key: str, value: str) -> dict | None:
    """
    Descripcion : reduce dos listas que estan en un diccionario en un nuevo diccionario

    params : 
        - dict (dict) : diccionario.
        - key (str) : clave con la lista que sera tomada como las key del nuevo diccionario.
        - value (str) : clave con la lista donde sus datos seran tomados como values en el nuevo dict.
    
    return (dict) : retorna un nuevo diccionario o None en caso de error
    """
    new_dict = {}
    i = 0
    try :
        for key, value in zip(dict[key], dict[value]):
            if key in new_dict:
                new_dict[f"{key} {i}"] = value
            else:
                new_dict[key] = value
            i += 1
    except KeyError:
        print("Introduce claves que sean validas")
        return None
    
    return new_dict


def reduce_list_dict(dict_list : list[dict]):
    """
    Descripcion : funcion que nos permite transformar una lista de diccionarios con la misma base de claves en un diccionario que tenga esa misma base de claves pero con una lista como valor, con cada uno de los datos que existia en cada uno de los diccionarios que coincida con la clave.

    ejemplo = [
    {key_1 : 2},
    {key_1 : 3},
    {key_1 : 5},
    ] 
    --->
    ejemplo = {
    key_1 : [2,3,5]
    }

    params :
        - dict_list (list[dict]) : lista con diccionarios 

    return dict : un diccionario con las estructuras transformadas
    """
    # Función para acumular los valores de cada clave
    def accumulator(acc, item):
        for key, value in item.items():
            value = str(value)
            if key in acc:
                acc[key].append(value)
            else:
                acc[key] = [value]
        return acc
    # Usamos reduce para acumular los valores de cada clave en un solo objeto
    reduced_dict = reduce(accumulator, dict_list, {})
    return reduced_dict


def reduce_dict(dct):
    """
    Reduzca un diccionario en el que los valores son listas, uniendo cada elemento de la lista con un guión.
    """
    return dict(map(lambda item: (item[0], "\n-".join(item[1])), dct.items()))


def sort_dict_by_value(d : dict):
    """
    descripccion : funcion que nos permite ordenar un diccionario atraves de sus valores.

    params :
        -d (dict[str : int | float]) : diccionario a ordenar

    return (dict) : nuevo diccionario ordenado
    """
    return dict(sorted(d.items(), key=lambda item: float(item[1])))

split_space = lambda string : string.split(" ")

def invertir_barras(ruta):
    """Description : funcion que toma una ruta con las barras \ en esta direccion e invierrte esta direccion (/)

    Params : 
        - ruta (str): una ruta que tenga las barra de esta manera \
        
    return (str) : retorna una ruta con las barras invertidas /
    """
    # Reemplazar las barras diagonales invertidas por barras diagonales normales
    ruta_con_barras_normales = ruta.replace("\\", "/")
    # Devolver la ruta invertida
    return "/".join(reversed(ruta_con_barras_normales.split("/")))

def transform_list_in_short_dictionary(data : list[dict], key : str, value):
    """Descripccion : funcion que nos permite tomar una lista de diccionarios con claves estandars y reducirla a un diccionario que tomtara un de los valores de una key como key y tome el valor de key como value.

    params : 
        - data : es la lista con los diccionarios 
        - key : es el nombre de la clave que sera tomada como key para los diccionarios 
        - value : es el nomre de la clave que sera tomada como valor
    
    return dict : un diccionario que tiene todos los datos pasados en los anteriores parametros estructurados como un solo diccionario con clave y valor 
    """

    new_obj = {}
    for index, obj in enumerate(data):
        if obj[key] in new_obj:
            new_obj[f"{obj[key]} {index}"] = obj[value]
        else:
            new_obj[obj[key]] = obj[value]
    return new_obj


if __name__ == "__main__":
    data = {'80101500': '1600.00', '80101500 1': '5000.00', "80101502" : '100.00'}
    
