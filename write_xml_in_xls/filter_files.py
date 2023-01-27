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

    
    def set_new_path(self, dir_path : str):
        self.__dir_path__ = dir_path


    def get_name_file(self, path_file: str):
        return path_file.split("/")[-1]


    def searh_files_by_directory(self, set_validation: set | list | tuple):
        set_validation = set(set_validation) if set_validation is not set else None

        set_validation_2 = re.compile("|".join(set_validation))
        files  = os.scandir(self.__dir_path__)

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

    def copy_file(self, new_dir :str, file : str):
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
    data_intereses = {"2235",
                          "2237",
                          "2238",
                          "2240",
                          "2241",
                          "2242",
                          "2243",
                          "2245",
                          "2246",
                          "2247",
                          "2248",
                          "2250",
                          "2251",
                          "2252",
                          "2255",
                          "2261",
                          "2262",
                          "2263",
                          "2264",
                          "2266",
                          "2267",
                          "2272",
                          "2274",
                          "2275",
                          "2276",
                          "2277",
                          "2280",
                          "2281",
                          "2282",
                          "2283",
                          "2284",
                          "2285",
                          "2286",
                          "2287",
                          "2288",
                          "2295",
                          "2300",
                          "2301",
                          "2302",
                          "2306",
                          "2330",
                          "2307",
                          "2319",
                          "2320",
                          "2321",
                          "2322",
                          "2323",
                          "2324",
                          "2325",
                          "2326",
                          "2327",
                          "2328",
                          "2329",
                          "2331",
                          "2332",
                          "2342",}

    Honorarios = {
"2236",
"2239",
"2249",
"2253",
"2254",
"2257",
"2258",
"2259",
"2260",
"2265",
"2268",
"2269",
"2270",
"2271",
"2273",
"2278",
"2289",
"2290",
"2294",
"2296",
"2297",
"2299",
"2303",
"2304",
"2305",
"2309",
"2310",
"2311",
"2312",
"2313",
"2314",
"2315",
"2316",
"2317",
"2318",
    }

    Arrendamientos = {"2244",
"2291",
"2292",
"2293",
"2298",}


    path = "read_CFDI/2022/11NOVIEMBRE"
    Noviembre_CFDI = Files(path)
    # list_filter_files = Noviembre_CFDI.filter_files("xml")
    # print(list_filter_files[0])
    # Noviembre_CFDI.move_list_file("XML", list_filter_files)

    Noviembre_CFDI.set_new_path(f"{path}/XML/")

    # data = Noviembre_CFDI.searh_files_by_directory(data_valitacion)
    # print(data)

    Honorarios_data = Noviembre_CFDI.searh_files_by_directory(Honorarios)
    Arrendamientos_data = Noviembre_CFDI.searh_files_by_directory(Arrendamientos)
    # Noviembre_CFDI.move_list_file("Intereses", data)
    Noviembre_CFDI.move_list_file("Honorarios", Honorarios_data)
    Noviembre_CFDI.move_list_file("Arrendamientos", Arrendamientos_data)


    

