from reedclients import reedClient
fidecomisos = reedClient("./Encargados_Fideicomisos.xlsx")
fidecomisos.set_sheet_name("Hoja2")

cell_nombres = fidecomisos._get_colum("NOMBRE")

Nombres = fidecomisos._get_values(cell_nombres)
Nombres = [nombre for nombre in Nombres if nombre != None]

numero_de_fidecomisos = round(len(Nombres))
la_mitad = round(numero_de_fidecomisos/2)

print(f"Numero de FIDECOMISOS asignados a mich y a mi {round(numero_de_fidecomisos/2)}")
print(f"limite Mich {Nombres[la_mitad]}")