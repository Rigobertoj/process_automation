import os
from reed_xml import RFC
from cfdi import CFDI
class multi_reed_xml():
    """
    descripcion : Clase que nos permite extraer la data de multiples xml que esten en un directorio

    params :
        - dir_path (str) : ruta donde se encuentran los CFDI xml
        - RFC (str) : RFC de la empresa dueña de los CFDI
    """
    __data__ = []
    def __init__(self, dir_path: str, RFC : str) -> None:
        self.dir_path = dir_path
        self.RFC = RFC


    def filter_file_dir_xml(self):
        documents = os.listdir(self.dir_path)
        
        def obtener_extencion_archivo(file : str):
            """
            descriptcion : funcion que me permite evaluar si un archivo es un XML 

            params : 
                file (str) : es el nombre del archivo

            return la extencion
            """
            document = file.split(".")
            if len(document) == 2 and document[1] == 'xml':
                return document[1]

        list_xml = list(
            map(lambda file : f"{self.dir_path}/{file}",
                filter(lambda file : obtener_extencion_archivo(file), documents)
            )
        )
        return list_xml

    def get_data_from_multiples_xml (self) :
        list_path_xml = self.filter_file_dir_xml()

        for file in list_path_xml:
            xml = CFDI(file, self.RFC)
            
            data = xml.main()         
            self.__data__.append(data)

        return self.__data__

    def get_data(self):
        self.get_data_from_multiples_xml()
        print(self.__data__)
        return self.__data__

if __name__ == '__main__':
    print("ENTER")
    dir_path = "./read_CFDI/2021/Enero/Recibidas"
    data = multi_reed_xml(dir_path, RFC)
    data_m = data.get_data()
    print(data_m)