import pandas as pd
import numpy as np

path_s = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/1.Ingresos/Proceso sistematizado"
path_m = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/1.Ingresos\Proceso manual"

mes = "Enero"

name_file_s = f"1.Ingresos.{mes}.xlsx"
name_file_m = f"1.Ingresos.{mes}.Manual.xlsx"

file_s = f"{path_s}/{name_file_s}"
file_m = f"{path_m}/{name_file_m}"
# print(file_s)

df_s = pd.read_excel(file_s, header=0)
df_m = pd.read_excel(file_m, header=0)

# Este pedaso de codigo solo se utilizo para el mes de Enero
df_s.drop(range(84, 92), inplace=True)

df_m["UUID"] = df_m["UUID"].apply(lambda folio : str(folio).lower())


set_UUID_s = set(df_s["UUID"])
set_UUID_m = set(df_m["UUID"])

Diferencias_s = set_UUID_s - set_UUID_m
Diferencias_m = set_UUID_m - set_UUID_s


def write_list_doc(data, name_file : str, title_file : str = None):
    with open(f"{name_file}", "w") as file:

        file.write(f"{title_file}")
        for array_list_text in data:
            for line_text in array_list_text:
                write_line_doc(line_text, file)
            


def write_line_doc(text : str, f):
    """
    Descripccion : funcion que nos permite escribir texto dentro de un file

    params :
        - text : es el texto que queremos pasar para escribirlo dentro del archivo
        - f : un tipo archivo

    return -> None
    """
    f.write(f"{text}\n")


if __name__ == "__main__":
    write_list_doc([Diferencias_m, Diferencias_s], "Diferencias de CFDI.txt")




# print(df_s)

# print(df_s)

print(len(Diferencias_m))
print(len(Diferencias_s))