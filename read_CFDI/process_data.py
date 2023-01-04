from reed_multiples_xml import multi_reed_xml
from reed_xml import reed_xml, RFC
import datetime

"""
fecha de estado de cuenta
fecha de factura 	
Tipo	
Clase	
Num Clase	
Folio fiscal	
nombre 	
concepto	
subtotal	
IEPS	 
IVA  	
Retenciones IVA 	
Retenciones ISR	Total	
Bancos


# Crea una cadena de texto con una fecha
fecha_texto = "2022-12-01T17:55:29"

# Define el formato de la fecha
formato_fecha = "%Y-%m-%dT%H:%M:%S"

# Transforma la cadena de texto en un objeto datetime utilizando strptime()
fecha = datetime.strptime(fecha_texto, formato_fecha)

"""




class Process_data():
    formato_fecha =  "%Y-%m-%dT%H:%M:%S"

    def __init__(self, dir_path : str, RFC : str) -> None:
        self.dir_path = dir_path
        self.RFC = RFC


    def crear_fecha(self, date: str) -> None:
        return datetime.datetime.strptime(date, self.formato_fecha)


    def process_xml_data(self,*data ):
        *_, data = data
        data_dict = {}
        data_dict["Tipo"] = data["Tipo"]
        data_dict["Fecha en el estado de cuenta"] = " "
        data_dict["Fecha factura"] = self.crear_fecha(data["Fecha"])
        data_dict["Operacion"] = " "
        data_dict["Clase"] = " "
        # TODO: realizar una evalucion sobre cual es el producto con el valor mas significantly
        # y asignar ese como Num Clase
        data_dict["Num Clase"] = " " 
        data_dict["Folio fiscal"] = data["Folio_fiscal"]
        
        
        if data["Tipo"] == "Recibido":
            data_dict["Nombre"] = data["Personas"]["Emisor"]["Emisor_name"]
        else:
            data_dict["Nombre"] = data["Personas"]["Receptor"]["Receptor_name"]

        
        
        conceptos = {}

        for data_concepto in data["Mount_prod_serv"]:
            clave_prod = data_concepto["Concepto"]["ClaveProdServ"]
            data_dict["Num Clase"] = clave_prod

            concepto_xml = data_concepto["Concepto"]["Descripcion"]
            price = data_concepto["Concepto"]["Importe"]

            if "Descuento" in data_concepto["Concepto"]:
                descuento = data_concepto["Concepto"]["Descuento"]
                conceptos[concepto_xml] = f"{concepto_xml} : {price} -{descuento} {clave_prod}, \n"
            else:
                conceptos[concepto_xml] = f"{concepto_xml} : {price} {clave_prod}"  

            data_concepto     
        
        lista_valores_conceptos = list(conceptos.values())

        concepto = " ".join(lista_valores_conceptos)   
        data_dict["Concepto"] = concepto
        
        data_dict["Sub total"] = data["Mount"]["SubTotal"]
        data_dict["Descuento"] = data["Mount"]["Descuento"]
        # data_dict["IEPS"] = data["Mount"]["IEPS"]
        # data_dict["IVA"]
        # data_dict["Ret. IVA."]
        # data_dict["Ret. ISR."]
        
        data_dict["Total"] = data["Mount"]["Total"]
        # print("Conceptos " + concepto_1)
        # print(data_dict)
        return data_dict
        




    def get_data(self) -> list[list, list]:
        multiples_lecturas_xmls = multi_reed_xml(self.dir_path, self.RFC)
        file_xml = multiples_lecturas_xmls.filter_file_dir_xml()

        for file in file_xml:
            xml = reed_xml(file, self.RFC)
            data = xml.get_data()
            data_process_xml= self.process_xml_data(data)
            print(data_process_xml)
            # for key, value in data_process_xml.items():
            #     print(value)
            #     if key == "Total": break 
            # print(data["Mount_prod_serv"][0]["Impuestos"]["Acreditables"])
            

if __name__ == '__main__':
    dir_path = "./CFDI/Testing_CFDI"
    conjunto_data_CFDI = Process_data(dir_path,RFC)
    data = conjunto_data_CFDI.get_data()
    print(data)