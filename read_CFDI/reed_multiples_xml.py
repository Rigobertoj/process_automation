import os
from reed_xml import reed_xml, RFC
class multi_reed_xml():
    """
    descripcion : Clase que nos permite extraer la data de multiples xml que esten en un directorio

    params :
        - dir_path (str) : ruta donde se encuentran los CFDI xml
        - RFC (str) : RFC de la empresa dueña de los CFDI
    """

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

    def reed_multiples_xml (self) :

        list_path_xml = self.filter_file_dir_xml()
        # re estructuracion funcioonal

        def extract_data(path : str):
            xml = reed_xml(path, self.RFC)
            return xml.get_data()

        data = list(map(lambda path: extract_data(path), list_path_xml))

        return data

if __name__ == '__main__':
    dir_path = "./CFDI/Testing_CFDI"
    data = multi_reed_xml(dir_path, RFC)
    print(len(data.reed_multiples_xml()))
