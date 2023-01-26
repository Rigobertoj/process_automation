import shutil
import os


class Files():
    """
    Descripcion :

    params : 
    """
    def __init__(self, dir_path : str,) -> None:
        self.dir_path = dir_path

    
    def get_name_file(self,path_file : str):
        return path_file.split("/")[-1]



    def filter_files(self, condicion : str):
        documents = os.listdir(self.dir_path)
        
        def obtener_extencion_archivo(file : str):
            """
            descriptcion : funcion que me permite evaluar si un archivo es un XML 

            params : 
                file (str) : es el nombre del archivo

            return la extencion
            """
            document = file.split(".")
            if len(document) == 2 and document[1] == condicion:
                return document[1]

        list_xml = list(
            map(lambda file : f"{self.dir_path}/{file}",
                filter(lambda file : obtener_extencion_archivo(file), documents)
            )
        )
        return list_xml

    def move_list_file(self, new_dir, list_path_file):
        if not os.path.exists(f"{self.dir_path}{new_dir}"):
            os.mkdir(f"{self.dir_path}{new_dir}")

        for file in list_path_file:
            new_dir_file = f"{self.dir_path}{new_dir}/{self.get_name_file(file)}"
            
            with open(file, "r")as origen, open(new_dir_file, "w") as destino:
                destino.write(origen.read())
                


    def move_file(self,new_dir, path_file):
        shutil.move(path_file, new_dir)


if __name__ == "__main__":
    path = "read_CFDI/2022/11NOVIEMBRE/"
    Noviembre_CFDI = Files(path)
    list_filter_files = Noviembre_CFDI.filter_files("xml")
    Noviembre_CFDI.move_list_file("XML", list_filter_files)

    # results = Noviembre_CFDI.get_name_file(list_filter_files[0])