from distutils.log import error
from pydoc import cli
from typing import List
from xml.dom.minidom import Element
import openpyxl
from convert import conver_value

PATH = "./Control de crédito mensual .xlsx"



# clase  que nos permite modificar las celdas de TIIE
class TIIE_file_edit_from_py ():
    """
    ?atributos:
        path_file (str) :  ruta por la cual se accedera y modificar el archivo excel
        Excel_document : instancia que permite manipular y modificar el doc excel
    ?class :
        clase la cual nos permite modificar y editar las secciones donde se hubica la tiie en un doc excel

        se empiza estableciendo la hoja con la cual se va atrabajar (set_shename)


    """
    def __init__(self, path_file: str):
        """
        constructor
        params:
            path_file (str) : ruta por la cual se accedera y modificar el archivo excel
        """
        # se define la ruta a la cual se accede
        self.path_file = path_file
        # se instancia una clase de openpyxl para cargar el archivo de la ruta
        self.Excel_document = openpyxl.load_workbook(path_file)
        self.conver_value = conver_value()


    #retorna una lista de las hojas existentes en un documento en excel
    def get_sheet_names(self) -> list:
        """
        metod:
            nos permite visualizar toda la lista de hojas de trabajo que tengamos en nuestro archivo excel

        retorn list : lista de las hojas existentes en el documento en excel

        """
        return self.Excel_document.sheetnames


    #establece la hoja con la que se va atrabajar
    def set_sheet_name(self, sheet_name: str):
        """
        params :
            sheet_name (str): nombre de la hoja con la cual se quiere trabajar

        metod:
            establace la hoja con la cual se va atrabar y tratar los datos
        """

        self.sheet_names = self.Excel_document[sheet_name]


    #retorna del objeto CELL la posicion donde esta la celda TIIE en una cadena de texto para su manipulacion
    def get_cell_as_string(self,cell_object):
        """
        params:
            cell (<Cell>) : es el tipo de dato cell que biene en openpyxl

        description:
            nos permite retornar del objeto CELL la cordenada o posicion del objeto eliminando el tipo, nombre de la hoja y los signos <>
        """
        #?objeto cell -> <Cell 'sheet name'.H15>

        #convertimos en un estring el objeto CELL
        element = self.conver_value.conver_string(cell_object)

        #separamos la cadena apartir del punto que viene en la cadena
        list_with_cell = element.split(".")

        #retornamos el segundo elemento que es la celda y quitamos el signo >
        #que esta en la ultima posicion del string
        cell = list_with_cell[1][0:-1]
        return cell


    #retorna un diccionario con un valor y una lista
    #el valor es la celda que almacena la columna de la TIIE
    def get_row(self, name_column: str ) -> dict | None:
        """
        params:
            name_column (str) : nombre de la culumna la cual bamos a buscar

        description:
            nos permite buscar una columna a partir de su nombre en una fila o algun dato string que este en ella si no existe el valor o la columna retorna None

        return dict : dict[value, list] list -> lista con la fila donde se encuentra el valor por el cuall buscamos la fila, value -> celda donde esta diccho valor
        """
        self.colum = {
            "value": 0,
            "list": list
        }
        #iteramos por cada fila en la hoja
        for row in list(self.sheet_names.rows):
            #iteramos por cada cellda en la fila
            for cell in row:

                #si el valor de la cellda es igual al dato que estamos buscando
                if cell.value == name_column:

                    #asignamos los valores al diccionario
                    self.colum["list"] = list(row) # fila donde se encuentra dicho valor
                    self.colum["value"] = cell # valor que se busca en el parametro
                    return self.colum
        



    #retorna un diccionario con un indice
    #EL INDICE es la posicon de la columna donde esta la TIIE
    def get_index_column(self, name_column: str):
        """
        params:
            name_column (str): titulo de la columna

        description:
            este metodo lo que nos mermite es obtener el indice donde se encuentra la columna es decir saber si la columna es la primera, segunda, tercera etc.
        """
        self.data_colum = int
        # obtenemos la fila donde se encuentra el valor que se busca
        row = self.get_row(name_column=name_column)

        if row == None:
            return None

        #del diccionario obtenemos los valores de la lista
        value_list = row["list"]

        #si no se encuntra la columna se retorna un error


        #iteramos por cada indice en la lista de celdas
        for i in range(len(value_list)):
            if(row["value"] == value_list[i]):
                self.data_colum = i

        print(self.data_colum)
        return self.data_colum

    # retorna dos listas
    # LA PRIMERA LIST es una lista de celdas las cuales tiene un valor asignado de TIIE
    # LA SEGUNDA LIST es una lista con las celdas las cuales no tiene un valor asignado

    def get_cells(self, name_column: str) -> dict:
        """
        params: 
            name_column (str): nombre de la columna que queremos extraer sus valores

        description:
            metodo que nos permite obtener una lista con las celdas que tienen los valores de la columna la cual buscamos
        """
        index_colum_TIIE = self.get_index_column(name_column)

        if index_colum_TIIE == None:
            return None
        
        #obtenemos la lista de valores del la hoja de excel
        list_column = list(self.sheet_names.columns)[index_colum_TIIE]
        #filtramos la lista por aquellos valores que su valor sea distinto a None
        lists_cells = list(filter(lambda x : x.value != None, list_column))

        return lists_cells


        #retorna la siguiente celda en la clumna la cual este vacia
    def get_next_cell_empty(self, name_column: str):
        """
        params:
            name_column (str) : nombre de la columa de la cual queremo obtener la ssiguinete celda vacia

            description :
                este metodo lp qie nos propociona es obtener la siguinete celda vacia en una columna 
        """
        #obtenemos las la lista de celldas de la columna
        lists_cell_value = self.get_cells(name_column)

        if lists_cell_value == None:
            return None
        #obtenemos la ultima cellda que tiene un valor
        last_cell_with_value = lists_cell_value[-1]

        #obtenemo la ultima celda que tiene un valor
        cell = self.get_cell_as_string(last_cell_with_value)
        print(f" empty cell {cell}")

        #desempaquetamos la el string cell
        print(f"celda {cell}")
        [letter ,*cord_x] = cell

        if len(cord_x) > 1:
            print(cord_x)
            cord_y = int(cord_x[1]) + 1
            cord_x[1] = cord_y
            cell = letter + cord_x[0] + str(cord_x[1])
        #despues a el valor que tiene la columna le sumamos uno
        #esto para que tenga el valor de siguiente celda vacia
        cord_y = int(cord_x[0])+1

        #volvemos ajuntar todo para retornarlo
        cell = letter + str(cord_x[0]) 
        return cell


    # inserta un valor float en la siguiente celda de la column TIIE
    def insert_value_in_client(self,value: float,):
        #TODO: realizar VALIDACIONES con respecto a la fecha para asi poder hacer una insercion de los datos a la fecha adecuada
        cell = self.get_next_cell_empty("TIIE")
        self.sheet_names[cell] = value
        self.Excel_document.save(self.path_file)

        print(self.sheet_names[cell].value)


if __name__ == "__main__":
    client = TIIE_file_edit_from_py(PATH)
    client.set_sheet_name("Ing Antonio Maravilla")

    # # client.conver_string(1)
    # cord = client.insert_value_in_client(.9)
    # value = conver_value(12)
    # tipe = value.conver_string()
    # print(type(tipe))
    # 
    
    # print(client.get_sheet_names())
    #     
    colum = client.get_row("TIIE")
    print(colum)