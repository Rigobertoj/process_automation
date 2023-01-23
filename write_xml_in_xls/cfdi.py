from reed_xml import Reed_xml, foreach
from functools import reduce
from typing import Optional, Union
import xml.etree.cElementTree as ET
import copy as c
from datetime import datetime


class CFDI (Reed_xml):
    def __init__(self, path_document : str, RFC : str, nombre : Optional[str] = "" ) -> None:
        super().__init__(path_document)
        self.__RFC__ = RFC
        self.__Nombre__ = nombre
        
    def main(self):
        
        fecha_De_facturacion = self.fecha_facturacion()
        self.conceptos = self.get_conceptos()
        Clave_de_producto_o_servicio = self.get_clave_prod_serv()
        Concepto_de_la_factura = self.get_invoice_concept()
        
        print(Clave_de_producto_o_servicio)
        return {
            "Fecha en el estado de cuenta." : None,
            "Fecha de facturación." : fecha_De_facturacion, 
            "Tipo.": None,
            "Clase." : None,
            "Clave de producto o servicio." : Clave_de_producto_o_servicio,
            "num" : None,
            "Folio fiscal." : None,
            "Nombre." : None,
            "Concepto." : Concepto_de_la_factura,
            "Subtotal." : None,
            "Descuentos." : None,
            "IEPS." : None,
            "IVA 16%." : None,
            "Ret. IVA." : None ,
            "Ret. ISR." : None,
            "Total." : None, 
            "Bancos.": None,
            "Folio relacionado" : None,
        }
    
    def convert_type_time(self, time_string : str):
        return datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S") 
    
    
    def fecha_facturacion(self):
        return self.convert_type_time(
            self.get_items(self.root, "Certificado")["Fecha"]
            )
        
    
    def get_conceptos(self):
        child_root = self.get_childs(self.root)
        conceptos = child_root["Conceptos"]
        concepto = self.get_items(
            self.get_childs(conceptos)["Concepto"]
            )
        
        
        
    def get_clave_prod_serv(self):
        return self.conceptos["ClaveProdServ"]
    
    
    def get_invoice_concept(self) -> str:
        return self.conceptos["Descripcion"]
    
    
    def Importe(self) -> str:
        return self.conceptos["Importe"]
    
    
    def sub_total(self) -> int :
        importe = int(self.conceptos["Importe"])
        if self.conceptos["Descuento"] :
            descuento = int(self.conceptos["Descuento"])
            return importe - descuento
        
        return importe 
    
    
    
if __name__ == '__main__':
    RFC = "PPR0610168Z1"
    fact_pago_emitida = "read_CFDI/2021/Enero/Emitidas/2f99dd73-df61-4481-bc02-34010db1fd3a.xml"
    fact_nomina = "read_CFDI/2021/Enero/Emitidas/10e2d438-f910-4036-874d-a9acc7504ca0.xml"
    fact_muchos_conceptos = "./read_CFDI/B9464F75-F69B-49FA-9A59-DB556505F669.xml"
    
    cfdi = CFDI(fact_muchos_conceptos,RFC)
    data = cfdi.main()
    # for key, value in data.items():
    #     print(
    #     f"""
    #     {key} : {value}
    #     """
    #     )