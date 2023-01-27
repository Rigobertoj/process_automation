import shutil
import os
import re


class Files():
    """
    Descripcion :

    params : 
    """

    def __init__(self, dir_path: str,) -> None:
        self.__dir_path__ = dir_path


    def set_new_path(self, dir_path: str):
        self.__dir_path__ = dir_path


    def get_name_file(self, path_file: str):
        return path_file.split("/")[-1]


    def filter_files_not_found(self, set_validation : set | list | tuple):
        set_validation = set(set_validation)
        files = os.scandir(self.__dir_path__)

        return {f"{self.__dir_path__}{file.name}" for file in files if all(val not in file.name for val in set_validation)}



    def searh_files_by_directory(self, set_validation: set | list | tuple):
        set_validation = set(
            set_validation) if set_validation is not set else None

        set_validation_2 = re.compile("|".join(set_validation))
        files = os.scandir(self.__dir_path__)

        
        return (file.path for file in files if set_validation_2.search(file.name))


    def filter_files(self, condicion: str):
        documents = os.listdir(self.__dir_path__)

        def obtener_extencion_archivo(file: str):
            """
            descriptcion : funcion que me permite evaluar si un archivo es un XML 

            params : 
                file (str) : es el nombre del archivo

            return la extencion
            """
            document = file.split(".")
            if len(document) == 2 and condicion in file:
                return document

        list_xml = list(
            map(lambda file: f"{self.__dir_path__}/{file}",
                filter(lambda file: obtener_extencion_archivo(file), documents)
                )
        )

        return list_xml


    def copy_file(self, new_dir: str, file: str):
        new_dir_file = f"{new_dir}/{self.get_name_file(file)}"

        with open(file, "r")as origen, open(new_dir_file, "w") as destino:
            destino.write(origen.read())

    def move_list_file(self, new_dir, list_path_file):
        if not os.path.exists(f"{self.__dir_path__}{new_dir}"):
            os.mkdir(f"{self.__dir_path__}{new_dir}")

        for file in list_path_file:
            self.copy_file(f"{self.__dir_path__}{new_dir}", file)

    def move_file(self, new_dir, path_file):
        shutil.move(path_file, new_dir)


if __name__ == "__main__":
    pass