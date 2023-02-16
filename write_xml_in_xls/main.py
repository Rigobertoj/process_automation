from process_data import  multi_reed_xml
from xls import xlsx
from reed_multiples_xml import multi_reed_xml


def get_xml_data(directorio,RFC):
    return multi_reed_xml(dir_path=directorio, RFC=RFC).get_data()


def insert_data(Document_path : str, file_name : str, name_sheet : str, initial_cell : int, data : list):
    wb = xlsx.write_xlsx(Document_path, file_name)
    keys = lambda row : wb.write_row_by_range(name_sheet, initial_cell, list(row.keys()))
    keys(data[0])
    value = list(map(lambda row : wb.write_row_by_range(name_sheet, initial_cell, list(row.values())), data))
    return value


def main():
    path_data = "C:/Users/rigoj/Documents/profile/contabilidad/2023/XML/Enero"
    xml_directorio_Egreos = f"C:/Users/rigoj/Documents/profile/contabilidad/2023/XML/Enero/Egresos"
    xml_directorio_Ingresos = f"{path_data}/Ingresos" 
    xls_directorio = f"{path_data}/Excel" 
    intial_cell = "A1"
    
    DATA_CFDI_Ingresos = get_xml_data(xml_directorio_Ingresos, RFC)
    # DATA_CFDI_Egresos = get_xml_data(xml_directorio_Egreos, RFC)
    insert_data(xls_directorio,"Ingresos.xlsx", name_sheet,intial_cell, DATA_CFDI_Ingresos, )
    # insert_data(xls_directorio, "Egresos.xlsx", name_sheet,intial_cell,DATA_CFDI_Egresos)


def data_2021() -> None:
    pass

def data_febrero_2023(RFC, name_sheet):
    path_recibidas = "C:/Users/User/Documents/Rigo/2023/XML/Recibidas/Febrero"
    path_emitidas = "C:/Users/User/Documents/Rigo/2023/XML/Emitidas/Febrero/Febrero"
    path_xlsx_recibidas = "C:/Users/User/Documents/Rigo/2023/Ingresos/Febrero"
    path_xlsx_emitidas = "C:/Users/User/Documents/Rigo/2023/Egresos/Febrero"



    Data_Emitidas = get_xml_data(path_emitidas,RFC)
    insert_data(
        path_xlsx_emitidas,
        "Febrero",
        name_sheet,
        "A1", 
        Data_Emitidas
        )
    del Data_Emitidas
    
    Data_recibidas = get_xml_data(path_recibidas, RFC)
    insert_data(        
        path_xlsx_recibidas,
        "Febrero",
        name_sheet,
        "A1", 
        Data_recibidas
        )
    del Data_recibidas
    

if __name__ == '__main__':
    RFC = "PPR0610168Z1"
    name_sheet = "Conjunto de gastos" 
    
    # main()
    # data_2021()
    data_febrero_2023(RFC, name_sheet)
    pass
