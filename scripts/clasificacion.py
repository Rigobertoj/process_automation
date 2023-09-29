import pandas as pd
import numpy as np
import openpyxl

dir_path = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/"
year = "2023"
month = "3.Marzo"
type_operation = "Ingresos"
name_working_paper = "3.Ingresos.Marzo.xlsx"

def return_dict(list):
    return {element : [] for element in list}


def get_columm(set_tipe, ws):
    set_operaciones = list
    for column in ws.columns: 
        for cell in column:
            if cell.value == f"{set_tipe}":
                set_operaciones = list(column)
                break
    return [cell.value for cell in set_operaciones]

def validate_and_remove_the_bar(texto):
    if '/' in texto:
        texto = texto.replace('/', '')
    return texto

def clasificacion(dir_path : str, year : str, month : str, type_operation : str, name_working_paper : str):
    year, month, type_operation, name_working_paper = map(validate_and_remove_the_bar, [year,
    month, type_operation,name_working_paper])

    # Ruta del ficheo
    path = f"{dir_path}{year}/{month}/{type_operation}/"

    # Crear un objeto Workbook de openpyxl
    wb = openpyxl.load_workbook(f"{path}{name_working_paper}")

    ws = wb["Conjunto de Ingresos"]

    # Crear una nueva hoja de Excel para la agrupación
    wb.create_sheet(title='Clasificacion ingresos')
    sheet = wb['Clasificacion ingresos']

    operaciones = get_columm("Tipo", ws)
    print(len(operaciones))

    dict_operaciones = return_dict(set(operaciones))


    def dict_rows(list_operaciones : list, dict_list : dict) -> dict[str : list]:
        for operacion, row in zip(list_operaciones, ws.rows):
            for key in list(dict_list.keys()):
                if key == operacion:
                    dict_list[key].append(row)

        print(len(list(dict_list["Intereses"])))
    
    print(dict_operaciones)

    dict_rows(operaciones, dict_operaciones)








if __name__ == "__main__":
    clasificacion(dir_path,year,month,type_operation,name_working_paper)




















