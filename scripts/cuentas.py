#Librerias de tranformacion  de datos
import pandas as pd
import numpy as np

#Ruta de donde se extrae la informacion.
path = "C:/Users/Luis Carlos Gomez/Rigoberto/Rigo.xlsx"

#Carga del Excel
df = pd.read_excel(path)

#funcion de convercion de dato a decimal
def convert_float(cuenta):
    if cuenta != np.NAN:
        return float(cuenta)
    return np.NAN

#Extraemos la columna IdAgrupadorSAT
#Aplicamos la funcion convert_float a cada elemento de la columna
#Retornamos la columna al mismo df
df["IdAgrupadorSAT"] = df["IdAgrupadorSAT"].apply(lambda cuenta : convert_float(cuenta))


#ordenamos el df en base a la columna IdAgrupadorSAT de manera asendente
df_sort = df.sort_values("IdAgrupadorSAT")

#Retornamos un archivo Excel en la siguiente ruta
df_sort.to_excel("C:/Users/Luis Carlos Gomez/Rigoberto/Rigo_Sort.xlsx")