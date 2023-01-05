from process_data import Process_data, reed_xml, multi_reed_xml
from write_xlsx import write_xlsx

def get_xml_data(directorio,RFC):
    response_data_xml = Process_data(dir_path=directorio, RFC=RFC)
    data = response_data_xml.get_data()
    return data


def process_xml_data(directorio, RFC):
    xml_data = get_xml_data(directorio,RFC)
    title = list(xml_data[-1   ].keys())
    values = list(map(lambda item : list(item.values()), xml_data))
    return {
        "title" : title,
        "values" : values
    }



def insert_data(xls_directorio : str,name_sheet : str, initial_cell : str ,matriz_data : list[list, list] | list):
    for rows in matriz_data:
        row, column = initial_cell
        wb = write_xlsx(path_file = xls_directorio)
        wb.write_row_by_range(name_sheet, row+column, rows)



if __name__ == '__main__':
    RFC = "PPR0610168Z1"
    xml_directorio = './read_CFDI/CFDI/enero/'
    xls_directorio = './xls/Enero_2022.xlsx'
    nome_sheet = "Clasificacion de gastos"
    name_sheet = "Conjunto de gastos"
    intial_cell = "A1"
    
    title, data_xml = process_xml_data(xml_directorio,RFC).values()
    
    insert_data(xls_directorio,name_sheet, intial_cell,[title])
    