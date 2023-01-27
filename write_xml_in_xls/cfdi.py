from reed_xml import Reed_xml, foreach
from functools import reduce
from typing import Optional, Union
import xml.etree.cElementTree as ET
import copy as c
from datetime import datetime


class CFDI (Reed_xml):
    __URL_CFDI__ = "{http://www.sat.gob.mx/cfd/3}"
    def __init__(self, path_document : str, RFC : str, nombre : Optional[str] = "" ) -> None:
        super().__init__(path_document)
        self.__RFC__ = RFC
        self.__Nombre__ = nombre
        self.root_attrs = self.get_items(self.root)
        print(self.root_attrs.get("Folio"))
        
    def test(self):
        print(self.get_taxes())
        
        
    def main(self):
        
        fecha_De_facturacion = self.fecha_facturacion()
        self.conceptos = self.get_conceptos()
        print(self.conceptos)
                    
        folio_fiscal = self.get_file_name()
        folio_de_la_factura = self.get_invoice_folio()
        Name = self.get_name()
        
        Descuentos = float(self.get_descuento())
        sub_total = float(self.get_sub_total())
        total = float(self.get_total())
        
        IVA, Ret_IVA, Ret_ISR = self.get_taxes()
        
        if self.searh_in_complement("Nomina"):
            Ret_ISR, Descuentos = self.get_data_nominas()
        
        
        Folio_fiscal_relacionado = self.get_folio_relaciones()
        
        return {
            "Fecha en el estado de cuenta." : None,
            "Fecha de facturación." : fecha_De_facturacion, 
            "Tipo.": None,
            "Clase." : None,
            "Clave de producto o servicio." : self.conceptos["Clave de producto o servicio."],
            "num" : folio_de_la_factura,
            "Folio fiscal." : folio_fiscal,
            "Nombre." : Name,
            "Concepto." : self.conceptos["Concepto"],
            "Subtotal." : sub_total,
            "Descuentos." : Descuentos,
            "IEPS." : None,
            "IVA 16%." : IVA,
            "Ret. IVA." : Ret_IVA ,
            "Ret. ISR." : Ret_ISR,
            "Total." : total, 
            "Bancos.": None,
            "Folio relacionado" : Folio_fiscal_relacionado,
        }
    
    def convert_type_time(self, time_string : str):
        return datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S") 
    
    
    def fecha_facturacion(self):
        return self.convert_type_time(
            self.get_items(self.root, "Certificado")["Fecha"]
            )
        
        
    def get_invoice_folio(self):
        return self.root_attrs.get("Folio")
        
    
    def get_name(self):
        Emisor, Receptor = self.Emisor_receptor()        
        return Receptor["Nombre"] if Emisor["Rfc"] == self.__RFC__ else Emisor["Nombre"]
        
    
    def Emisor_receptor(self):
        """Descripcion : Metodo que nos permite extraer 2 diccionarios con los atributos de los elementos Emisor y Receptor

        Returns:
            Tubla[Dict, Dict]: Tupla con el diccionario Emisor y Receptor en ese orden
        """
        Emisor = self.get_items(self.get_childs(self.root)["Emisor"])
        Receptor = self.get_items(self.get_childs(self.root)["Receptor"])
        
        return (Emisor, 
                Receptor)
    
        
    def get_concepto(self, element : ET.Element):
        return self.get_items(element)
    
    
    def get_conceptos(self) -> dict: 
        return self.reduce_dict(
            self.reduce_list_dict(
                self.Data_conceptos()
                )
            )
    
    
    def Data_conceptos(self):        
        child_root = self.get_childs(self.root)
        conceptos = child_root["Conceptos"]
                
        Data_conceptos = list(map(self.get_concepto, list(conceptos)))
            
        return list(map(self.compuse_data_conceptos, Data_conceptos))
    
        
    def compuse_data_conceptos (self, data_element : dict):
        ClaveProdServ = self.get_clave_prod_serv(data_element)
        Descripcion = self.get_invoice_concept(data_element)
        Importe = self.get_Importe(data_element)
        Descuento = self.get_concep_descuento(data_element)
        Sub_total = self.get_sub_total_concept(data_element)
        
        return {
            "Clave de producto o servicio." : ClaveProdServ,
            "Concepto" : Descripcion,
            "Importe" : Importe,
            "Sub total" : Descuento,
            "Sub total" : Sub_total,
        }
        
    def reduce_list_dict(self, dict_list):
        # Función para acumular los valores de cada clave
        def accumulator(acc, item):
            for key, value in item.items():
                value = str(value)
                if key in acc:
                    acc[key].append(value)
                else:
                    acc[key] = [value]
            return acc

        # Usamos reduce para acumular los valores de cada clave en un solo objeto
        reduced_dict = reduce(accumulator, dict_list, {})

        return reduced_dict

    def reduce_dict(self, dict) -> dict:
        c_dict = c.copy(dict)
        for key, value in c_dict.items():
            c_dict[key] = "\n".join(value)
        return c_dict
        

    def get_clave_prod_serv(self, data_element : dict):
        if data_element["ClaveProdServ"]:
            return data_element["ClaveProdServ"]
        return None
    
    def get_invoice_concept(self,  data_element : dict) -> str:
        return data_element.get("Descripcion")
    
    
    def get_Importe(self, data_element : dict) -> str:
        return data_element.get("Importe")
    
    
    def get_sub_total_concept(self,  data_element : dict) -> float :
        importe = float(data_element["Importe"])
        
        if "Descuento" in data_element:
            descuento = float(data_element["Descuento"])
            return importe - descuento
        
        return importe 
    
    
    def get_concep_descuento(self, data_element):
        return data_element.get("Descuento")
    
    
    def get_sub_total(self):
        return self.root_attrs.get("SubTotal")


    def get_descuento(self):
        return self.root_attrs["Descuento"] if "Descuento" in self.root_attrs else 0
    
    
    def get_total(self):
        return self.root_attrs["Total"]
    
    
    def get_retenciones(self) -> int:
        try :
            Impuestos = self.root.find(f"{self.__URL_CFDI__}Impuestos")
            
            if not Impuestos:        
                return None
            
            Retenciones = Impuestos.find(f"{self.__URL_CFDI__}Retenciones")
            
            if not Retenciones:
                return None
            
            elements = self.get_childs(Retenciones)
            data_elements = list(map(self.get_items, list(elements.values())))
            return {obj["Impuesto"] : obj["Importe"] for obj in data_elements}
            
        except KeyError or AttributeError:
            print(F"ERROR: get_retenciones -> {self.get_retenciones()}")
            return None
        
    def search_tag(self, name_tag : str, element : ET.Element):
        try :
            return lambda URL : next(
                filter(
                    lambda e: e.tag == f"{URL}{name_tag}", element.iter()
                    )
                )
        except StopIteration :
            return None
        
    def get_traslado(self) -> dict[str]:
        try :
            
            Impuestos = self.root.find(f"{self.__URL_CFDI__}Impuestos")
            
            if not Impuestos:
                return None
            
            Traslados = Impuestos.find(f"{self.__URL_CFDI__}Traslados")
            Traslado = self.get_childs(Traslados)       
            

        
            Retencion = list(map(self.get_items, list(Traslado.values())))
            data_traslados= list({objeto['Impuesto'] : float(objeto['Importe']) for objeto in Retencion}.values())
            return reduce( lambda acc, current_value : acc + current_value, data_traslados) 
        except KeyError or AttributeError:
            print(F"ERROR: get_traslado -> {self.get_retenciones()}")
            return None
        
        except StopIteration :
            print(F"ERROR: get_traslado -> {self.get_retenciones()}")
            return None
    
        
    def get_taxes(self):
        """Descripcion : metodo que nos permite obtener de manera estructurada los impuestos de la factura

        Returns:
            Tupla[int | None, int | None, int | None]: Retornamos una tupla con los valores del IVA, Ret de IVA y Ret de ISR en ese orden
        """
        
        traslado = self.get_traslado() 
        ret = self.get_retenciones() or {}

        return traslado, ret.get("002"), ret.get("001"),
        
            
    
    
    def searh_in_complement(self, name_tag : str):
        try:
            child_root = self.get_items(self.get_childs(self.root))
            child_complemento = self.get_items(self.get_childs(child_root.get("Complemento")))
            return name_tag in child_complemento
            
        except (AttributeError, KeyError):
            return False 
    
    
    def get_data_nominas(self):
        """Descripcion : Metodo que nos permite obtener los impuestos o deducciones que se le realizan a la nomina en cada una de las operaciones
        
        Return (Tuple[])
        
        """
        
        Impuestos = {}
        get_data = lambda e : self.get_items(self.get_childs(e))
        try :
            
            Complemento = get_data(self.root)["Complemento"]
            concept_complemento = get_data(Complemento)
            Data_nomina = get_data(concept_complemento["Nomina"])
            Deducciones = get_data(Data_nomina["Deducciones"])
            
            data_deducciones = list(
                map(self.get_items, list(Deducciones.values()))
                )           
        except AttributeError:
            
            return None
        
        Impuestos = {Deducion["TipoDeduccion"] : Deducion["Importe"]  for Deducion in data_deducciones}
        
        
        ISR = Impuestos.get("002")
        IMSS = Impuestos.get("004")

        return ISR, IMSS
        
    def get_folio_relaciones(self):
        try :
            return next(
                filter(
                    lambda element: element.tag == "{http://www.sat.gob.mx/Pagos}DoctoRelacionado", self.root.iter()
                    )
                ).get("IdDocumento")
        except StopIteration :
            return None
        
        
        
        
    
if __name__ == '__main__' :
        
    RFC = "PPR0610168Z1"
    fact_pago_emitida = "read_CFDI/2021/Enero/Emitidas/2f99dd73-df61-4481-bc02-34010db1fd3a.xml"
    fact_nomina = "read_CFDI/2021/Enero/Emitidas/10e2d438-f910-4036-874d-a9acc7504ca0.xml"
    fact_muchos_conceptos = "./read_CFDI/B9464F75-F69B-49FA-9A59-DB556505F669.xml"
    fact_honorarios = "./read_CFDI/AAA19A00-5E5C-4A80-973B-3F3022AD76DC.xml"
    fact_nomina_2 = "./read_CFDI/Nomina/E211FFAB-D67D-4373-968E-83C02741628F.xml"
    problemas_iva = "read_CFDI/2021/Enero/Recibidas/26cadc4a-b591-4912-911e-20a57252de24.xml"
    Problemas_complemento = "read_CFDI/2021/Enero/Recibidas/1ab75101-13d5-4a88-ab93-3e123df5b38b.xml"
    
    cfdi = CFDI(Problemas_complemento,RFC)
    data = cfdi.main()
    for key, value in data.items():
        print(
        f"""
        {key} : {value}""")