import pandas as pd
import numpy as np

mes = "Marzo"

#Ruta del archivo con los datos
path_2022 = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/1.Ingresos/Proceso sistematizado/octubre.diot.xlsx"
path_2023 = f"C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2023/{mes}/Egresos"

# carga del archivo en un Data Frame (df)
df = pd.read_excel(f"{path_2023}/3.Egresos.Marzo.xlsx", header=0)

# df = df.sort_values("subtotal")

df_groupby_rfc = df.groupby("RFC Emisor")

df_gropby_rfc = pd.DataFrame(df_groupby_rfc["Subtotal"].sum())

# df_gropby_rfc["RFC Emisor"].apply(lambda RFC : str(RFC))

print(df_gropby_rfc.head(1))

# df_gropby_rfc.to_excel(f"{path_2023}/DIOT.Marzo.xlsx")

df_gropby_rfc_Emisor = pd.DataFrame(df_groupby_rfc["Nombre Emisor"])
df_gropby_rfc_Emisor.columns = ["RFC Emisor", "Nombre Emisor",]
print(df_gropby_rfc_Emisor["RFC Emisor"])

# print(df_gropby_rfc_Emisor.to_excel(f"{path_2023}/DIOT.TEST.xlsx"))
# print("data",df_gropby_rfc_Emisor.describe())

df_join = df_gropby_rfc.merge(df_gropby_rfc_Emisor, left_index="RFC Emisor", right_index="RFC Emisor")
print(df_join)

print("La suma de los egresos es: ${:,.2f}".format(df_gropby_rfc["Subtotal"].sum()))