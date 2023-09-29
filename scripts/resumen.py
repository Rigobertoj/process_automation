import pandas as pd
import numpy as np
import locale

# Establecer el formato de localización para el dinero
locale.setlocale(locale.LC_ALL, 'es-MX')

# rutas del documento excel
dir_path = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/"
year = "2023"
month = "3.Marzo"
type_operation = "Ingresos"
name_working_paper = "3.Ingresos.Marzo.xlsx"

def resumen_ingresos_gastos(dir_path : str, year : str, month : str, type_operation : str, name_working_paper : str):
    path = f"{dir_path}{year}/{month}/{type_operation}/"

    # Leer solo las columnas necesarias del archivo Excel
    columns_to_read = ['Tipo', 'Subtotal', 'Base Traslado', 'Total IVA Trasladado', 'Total IVA Retenido', 'Total ISR Retenido', 'Total']

    # Leemos el archivo excel con las columnas antes mencionadas
    df = pd.read_excel(f"{path}/{name_working_paper}", usecols=columns_to_read)

    # Agrupamos los datos por tipo de operacion
    # aplicamos una funcion de suma a cada una de las columnas para obtener el importe total
    resumen_ingresos_gastos = df.groupby("Tipo").agg(
        {'Subtotal': 'sum', 
        'Base Traslado': 'sum',
        'Total IVA Trasladado': 'sum', 
        'Total IVA Retenido': 'sum', 
        'Total ISR Retenido': 'sum', 
        'Total': 'sum'}
        )
    
    print("")
    # Aplicamos una funcion que nos permite darle un formato de pesos 
    # Imprimimos dicha informacion
    print(resumen_ingresos_gastos.applymap(lambda importe : locale.currency(importe, grouping=True) ))
    
    # Mandamos la data a un excel
    resumen_ingresos_gastos.to_excel(f"{path}/Resumen ingresos 2.xlsx")

if __name__ == "__main__":
    resumen_ingresos_gastos(dir_path,year,month,type_operation,name_working_paper)