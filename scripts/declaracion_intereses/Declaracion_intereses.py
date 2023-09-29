import pandas as pd
import numpy as np
import openpyxl

def not_nan(conjunto):
    return list(filter(lambda element : element != None, conjunto))


# TODO : realizar un meotodo que valide sobre los importes de cada columna con el objetivo de que no cuadren las cifras

class Declaracion_intereses():
    """
    Description : Clase que me permite procesar el archivo de la declaracion de intereses con el fin de porder transformarlo en un .txt

    params :
        - path_file : es la ruta donde esta el archivo con los datos

    Complement :
        - file : dicho archvo debe de tener 4 hoja con los siguientes nombre de manera exacta
            - 1. REGISTRO DE ENCABEZADO
            - 2. REGISTROS DE DETALLE
            - 3. DETALLE DE DOMICILIOS
            - 4. REGISTRO SUMARIO
        con los elementos que establesca el area de credito

        - Content : el contenido de los registro no debe o en su mayoria no tiene que tener datos nulos.
        Cada uno de los registros que deba de ser tomado en cuenta para la extraccion debe de contener en la columna inicial osea A (AX) un pipe -> '|'  
    """
    # self -> 
    def __init__(self, path_file) -> None:
        # ruta del documento
        self.__path_file__ = path_file
        
        #cargamos el papel de trabajo
        self.wb = openpyxl.load_workbook(path_file)
        
        # se obtiene cada una de las hojas del excel (MATRIZES DE DATOS)
        self.REGISTRO_DE_ENCABEZADO  = self.wb["1. REGISTRO DE ENCABEZADO"]
        self.REGISTROS_DE_DETALLE = self.wb["2. REGISTROS DE DETALLE"]
        self.DETALLE_DE_DOMICILIOS = self.wb["3. DETALLE DE DOMICILIOS"]
        self.REGISTRO_SUMARIO = self.wb["4. REGISTRO SUMARIO"]

        # se obtiene cada uno de los df del excel (DATA FRAME)

        #.dropna(how='all', inplace=True)
        self.DF_REGISTROS_DE_DETALLE = pd.read_excel(path_file, sheet_name="2. REGISTROS DE DETALLE", header=1)

        self.DF_DETALLE_DE_DOMICILIOS = pd.read_excel(path_file, sheet_name="3. DETALLE DE DOMICILIOS", header=1)

        
        self.__validation_accredited__()

    def __get_registro__(self, rows):
        """
        Description : Metodo que nos 
        """
        data = []
        for row in rows:
            for cell in row:
                if cell.value == "|":
                    data.append([str(cell.value) for cell in row][1:-1])
        return data
    
    def __format_txt__(self, registro_data : list[str]) -> str:
        """
        Description : Metodo que me permite darle el formato con los pipes a cada elemento de una lista que representa una celda de una fila.

        params:
            - registro_data (list[str]) : lista con las celdas de la fila del excel.

        return (str): string que reduce los elementos de la lista separados por un pipe (word|word |word)  
        """
        registro_txt = '|'.join(registro_data)
        if "None" in registro_txt:
            registro_txt = registro_txt.replace("None", "")
            return registro_txt
        
        return registro_txt
        

    def __get_encabezado__(self) -> list[str]:
        return self.__get_registro__(self.REGISTRO_DE_ENCABEZADO.rows)[0]  
    
    def __get_registro_detalle__(self) -> list[list[str]]:
        return self.__get_registro__(self.REGISTROS_DE_DETALLE.rows)
    
    def __get_detalle_domicio__(self) -> list[list[str]]:
        return self.__get_registro__(self.DETALLE_DE_DOMICILIOS.rows)
    
    def __get_registro_sumario__(self) -> list[str]:
        return self.__get_registro__(self.REGISTRO_SUMARIO.rows)[0]
    
    def __validation_interest_amount__():
        
        return
    

    def __validation_accredited__(self,):
        data_registro = self.__get_registro_detalle__()
        data_domicilio = self.__get_detalle_domicio__()

        print(self.DF_REGISTROS_DE_DETALLE.info())
        try:
            conjnto_acreditados_registro_detalle = set(not_nan(self.DF_REGISTROS_DE_DETALLE["RFC"]))
            conjnto_acreditados_detalle_domicilio = set(not_nan(self.DF_DETALLE_DE_DOMICILIOS["RFC"]))
        except:
            KeyError("Valida que la columna RFC no tenga espacio o este bien escrita")
            pass
        # Diferencia de conjuntos
        dif_detalle_mens_domicilio = conjnto_acreditados_registro_detalle - conjnto_acreditados_detalle_domicilio
        
        dife_domicilio_mens_detalle = conjnto_acreditados_detalle_domicilio - conjnto_acreditados_registro_detalle
        if (len(dif_detalle_mens_domicilio) != 0) or ( len(dife_domicilio_mens_detalle) != 0):
            print("Logitud de registros en las hojas de excel :")
            print(f"domicilio   {len(data_domicilio)}")
            print(f"registro    {len(data_registro)}")
            print("")
            print(f"Registro de detalle menos detalle de domicilio {dif_detalle_mens_domicilio}")
            print(f"Detalle de domicilio menos registro de detalle {dife_domicilio_mens_detalle}")
            print("")
            raise "Existen difenciar entre los conjuntos de acreditados que se establecen en los papeles de trabajo"

    def TXT(self):
        Encabezado = self.__get_encabezado__()
        Encabezado_txt = self.__format_txt__(Encabezado)
        with open("Declaracion de intereses 2.txt", "w", encoding="UTF-8") as D:
            D.write(f"{Encabezado_txt}|\n")
            
            data_registro = self.__get_registro_detalle__()
            data_domicilio = self.__get_detalle_domicio__()            

            for resgistro, domicilio in zip(data_registro,data_domicilio):
                resgistro_txt = self.__format_txt__(resgistro)
                domicilio_txt = self.__format_txt__(domicilio)

                D.write(f"{resgistro_txt}|\n")
                D.write(f"{domicilio_txt}|\n")
            
            registro_sumario = self.__get_registro_sumario__()
            registro_sumario_txt = self.__format_txt__(registro_sumario)

            D.write(registro_sumario_txt)

    def __str__(self) -> str:
        return f"{self.__path_file__}"
    

    def __test__(self):
        return 



if __name__ == "__main__":
    # Interés nominal (GRAVADO)
    path = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/Declaracion.intereses.xlsx"
    Declaracion_intereses_2021 = Declaracion_intereses(path)
    a = Declaracion_intereses_2021.__test__()
    print(a)