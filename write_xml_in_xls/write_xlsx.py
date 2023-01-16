import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import os
import copy


class write_xlsx():
    """
    description: clase la cual nos proporciona metodo para la escritura y manipulacion de archivos excel

    attributes:
        path_file (str) : excel document path
        Excel_document (load_workbook): instancia de la clase load_workbook con el doc excel
        sheet_name ( str ) : nombre de la hoja para manipular



    """
    
    sheets = {}
    item = 1

    def __init__(self, name_woorkbook = "", path_file = "",  ) -> None:

        """
        description: crea un nuevo documento con el cual se va a trabajar o establece el document que se manipulara.

        si deseas cargar un archivo ya existente pasarias el argumento de file_path o si desear crear uno nuevo el argumento de name_woorkbook

        param:
            - name_woorkbook (str) : Nombre del documento que se va a crear o trabajar
            - file_path (str) : excel document path


        """
        try :
            print("try")
            if name_woorkbook  != "":
                print("workbook")
                self.wb = Workbook(name_woorkbook)
                print(self.wb)
                self.__path_file = name_woorkbook
            elif path_file != "":
                print("loading path")
                print(self.item)
                self.wb = load_workbook(path_file)
                print("WB ")
                self.__path_file = path_file
        except: ValueError("Introduce una ruta o nombre de archivo valido")




    def get_shenames(self) -> list[str, str]:
        """
        description:
            retorna una lista con los nombres de las hojas que contiene el documento introducido

        return (list) : lista con los nombres de las hojas del documento
        """
        print(self.wb.sheetnames)
        return self.wb.sheetnames



    def set_sheet_name(self, sheet_name: str,) -> str:
        """
        description: establece la hoja del documento que se procesara o manipulara

        params:
            - sheet_name (str) : nombre de la hoja en el documento

        return (str) : nombre de la hoja en el documento
        """
        self.sheet_name = self.wb[sheet_name]
        return self.sheet_name


    def write_row_by_range(self, name_sheet :str, initial_cell : str, data = list, ):
        
        """
        descripcion : metodo que nos permite modficar una fila a tarves de una lista con datos que queremos que sean asignados
        a las celdad de forma ordenda 

        al pasar la lista se toma la longitud de esta para saber cuantos datos a partir de la ceda dada como parametro "initial_cell" se necesitan modificar e iterar por la misma asignando a cada celda un dato de la lista

        params :
            - name_sheet (str) : establece la hoja o crear una nueva donde se ballan a escribir datos 
            - initial_cell (str) : celda de la cual quieres partir la insercion de datos (ejemplo : "A1","B3" etc. )
            - data (list) : datos los cuales quieres insertar en la fila
        """
        def letra_a_numero(letra):
            if len(letra) == 1:
               return ord(letra) - ord('A') + 1
            else:
                print("else")
                return 26 * letra_a_numero(letra[:-1]) + letra_a_numero(letra[-1])
            
        def asigacion_de_data(data,cell):
            cell.value = data
            return cell
           
        #obtenemos la columna desde que se empezada
        colunn = initial_cell[0]
        
        #obtenemos la fila a editar
        row = int(initial_cell[-1]) 

        #obtenemos el numero de la culumna donde esta esa celda
        num_column = letra_a_numero(colunn)
        
        #obtenemos el maximo de celdad que se van a escribir
        max_col = num_column + len(data) -1
        
        if name_sheet in self.wb.sheetnames:
            self.ws = self.wb[name_sheet]
        else:
            self.ws = self.wb.create_sheet(name_sheet)

        # celda inicial y celda final del rango a escribir
        def rows_iter(row, num_column, max_col):
            fila_a_editar = self.ws.iter_rows(
            min_row=row, max_row=row, min_col=num_column, max_col=max_col
            )
            
            
            fila_validada = self.Empty_row(fila_a_editar)
            
            print(f"Fila_vasia {fila_validada}")
            
            if fila_validada:
                print("if ")
                return fila_validada
            else:
                print("else")
                return rows_iter(row + 1, num_column, max_col)
            
        fila_a_editar = rows_iter(row, num_column, max_col)
        fila_a_editar = fila_a_editar[0]
        print(fila_a_editar)
        value = list(
            map(asigacion_de_data, 
            data,
            fila_a_editar
        ))
        print(f"value {value}")
        self.wb.save(self.__path_file)
        
    def Empty_row (self, fila_a_editar):
        validate = {True}

        copi_row = copy.copy(list(fila_a_editar))
        print(copi_row)
        for row in copi_row:
            for cell in row:
                if cell.value != None:
                    validate.add(False)
                    
        if False  not in validate:
            return copi_row
        
        return False            
            

if __name__ == "__main__":
    enero = write_xlsx(path_file="./xls/Enero_2022.xlsx")
    enero.write_row_by_range("Clasificacion de gastos", "A2", ["2","3"])
