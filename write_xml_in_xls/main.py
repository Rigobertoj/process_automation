from process_data import Process_data, reed_xml, multi_reed_xml
from write_xlsx import write_xlsx
from reed_multiples_xml import multi_reed_xml

def get_xml_data(directorio,RFC):
    response_data_xml = multi_reed_xml(dir_path=directorio, RFC=RFC)
    return response_data_xml.get_data()


def insert_data(Document_path : str, name_sheet : str, initial_cell : int, data : list):
    wb = write_xlsx(Document_path)
    keys = lambda row : wb.write_row_by_range(name_sheet, initial_cell, list(row.keys()))
    data_kesy = keys(data[0])
    value = list(map(lambda row : wb.write_row_by_range(name_sheet, initial_cell, list(row.values())), data))
    return value

if __name__ == '__main__':
    RFC = "PPR0610168Z1"
    xml_directorio = "./read_CFDI/2021/Enero/Emitidas"
    xls_directorio = './xls/Enero_2022.xlsx'
    name_sheet = "Conjunto de gastos"
    intial_cell = "A1"
    
    DATA_CFDI = get_xml_data(xml_directorio, RFC)
    # for element in DATA_CFDI:
    #     print("_____________________________________________________________")
    #     for key, value in element.items():
    #         print(f"""
    #               {key} {value}""")
    insert_data(xls_directorio, name_sheet,intial_cell, DATA_CFDI)