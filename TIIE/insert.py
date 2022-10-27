import os
from edit_file_credit import TIIE_file_edit_from_py
from getTIIE import TIIE_Actual

class insert_data():
    def __init__(self, path_file: str, sheet_name: str) -> None:
        """
        params:
            path_file (str): path to excel document
            sheet_name (str): name of excel sheet to work and insert data
        
        description: 
            initial the instantiate document excel, whit the sheet name, to allows insert the data from TIIE and save inteh same path file 

        """
        #del objeto de la TIIE solo obtenemos el dato actual
        TIIE = TIIE_Actual()["dato"]

        #instanciamos el documento excel para trabajar con el y manipularlo
        client = TIIE_file_edit_from_py(path_file)

        #establecemos la hoja con la cual bamos a trabajar
        client.set_sheet_name(sheet_name)
        print(client.sheet_names)
        "insert the tiie in the document excel file confirm to open the file and view the data en column with the name TIIE "
        client.insert_value_in_client(TIIE)


if __name__ == "__main__":
    path = "./Control de crédito mensual .xlsx"
    sheet_name = "Alejandro Ochoa"
    control_credito = insert_data(path_file=path,sheet_name=sheet_name)
    print(path)