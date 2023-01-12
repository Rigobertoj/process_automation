from reed_xls import reed_xlsx
from circulo_credito_xml import circulo_credito

Data_otorgante = {
        "ClaveOtorgante" : "0000080008",
        "NombreOtorgante" : "PROMOTORA PROFILE",
        "IdentificadorDeMedio" : "AZ",
        "FechaExtraccion" : 20210630,
        "NotaOtorgante" : "",
        
    }

work_file_name = "BASE DE DATOS CIRCULO DE CREDITO"
sheet_name = "Info_creditos"
XML = reed_xlsx(f"./{work_file_name}.xlsx", sheet_name)
data_acrediatnte = XML.get_data_row()[0]

# for key,value in data_acrediatnte.items():
#     print(f"{key}  \t{value}")

XML = circulo_credito(
    Data_otorgante["ClaveOtorgante"],
    Data_otorgante["NotaOtorgante"], 
    Data_otorgante["FechaExtraccion"],
    [data_acrediatnte]
    )
XML.get_doc()