from reed_multiples_xml import multi_reed_xml, dir_path
from reed_xml import reed_xml, RFC

class Extrac_data():
    def __init__(self, dir_path : str, RFC : str) -> None:
        self.dir_path = dir_path
        self.RFC = RFC
    
    def get_data(self) -> list[list, list]:
        data = multi_reed_xml(self.dir_path, self.RFC)
        print(data)

    
    def get_data_from_file():
        reed_xml()


if __name__ == '__main__':
    conjunto_data_CFDI = Extrac_data(dir_path,RFC)
    data  = conjunto_data_CFDI.get_data()