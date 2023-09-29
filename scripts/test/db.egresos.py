import pandas as pd
path = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/Conjunto de egresos 2022.xlsx."

df = pd.read_excel(path)
conjunto_operaciones = set(df["Tipo de operación."])

with open("operaciones.txt", "w", encoding="UTF-8") as f:
    for operaciones in conjunto_operaciones:
        f.write(f"{operaciones}\n")