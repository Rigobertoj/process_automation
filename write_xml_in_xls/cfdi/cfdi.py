from reed_xml import Reed_xml, foreach
from utils import utils, maybe
from functools import reduce
from typing import Optional, Union
import xml.etree.cElementTree as ET
import copy as c
from datetime import datetime


class CFDI (Reed_xml):
    def __init__(self, path_document: str, RFC: str, nombre: Optional[str] = "") -> None:
        super().__init__(path_document)
        self.__RFC__ = RFC
        self.__Nombre__ = nombre
        self.root_attrs = self.get_items(self.root)

    def test(self):
        data = self.get_clave_prod_serv()



    def main(self):
        self.__get__url_CFDI__()
        fecha_De_facturacion = self.fecha_facturacion()

        self.conceptos = self.get_conceptos()

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
            "Fecha en el estado de cuenta.": None,
            "Fecha de facturación.": fecha_De_facturacion,
            "Tipo.": None,
            "Clase.": None,
            "Clave de producto o servicio.": self.get_clave_prod_serv(),
            "num": folio_de_la_factura,
            "Folio fiscal.": folio_fiscal,
            "Nombre.": Name,
            "Concepto.": self.conceptos["Concepto"],
            "Subtotal.": sub_total,
            "Descuentos.": Descuentos,
            "IEPS.": None,
            "IVA 16%.": IVA,
            "Ret. IVA.": Ret_IVA,
            "Ret. ISR.": Ret_ISR,
            "Total.": total,
            "Bancos.": "=J2-K2+L2+M2-N2-O2=P2",
            "Folio relacionado": Folio_fiscal_relacionado,
        }

    def convert_type_time(self, time_string: str):
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

    def get_clave_prod_serv(self,):
        """
        descripcion : Metodo que me permite obtener la clave de producto o servicio en base a el producto o servicio que tenga mayor proporcion en la factura

        return (str) : clave de producto o servicio
        """
        data = utils.reduce_list_dict(
            self.Data_conceptos()
        )
        dict_data = utils.reduce_two_list_dict(
            data, "Clave de producto o servicio.", "Importe")
        dict_sort = utils.sort_dict_by_value(dict_data)
        key = list(dict_sort.keys())[-1]
        return utils.split_space(key)[0]

    def get_concepto(self, element: ET.Element):
        return self.get_items(element)

    def get_conceptos(self) -> dict:
        data = utils.reduce_dict(
            utils.reduce_list_dict(
                self.Data_conceptos()
            )
        )
        return data

    def Data_conceptos(self):
        child_root = self.get_childs(self.root)
        conceptos = child_root.get("Conceptos")

        Data_conceptos = list(map(self.get_concepto, list(conceptos)))

        data = list(map(self.compuse_data_conceptos, Data_conceptos))
        return data

    def compuse_data_conceptos(self, data_element: dict):
        ClaveProdServ = self.set_clave_prod_serv(data_element)
        Descripcion = self.get_invoice_concept(data_element)
        Importe = self.get_Importe(data_element)
        Descuento = self.get_concep_descuento(data_element)
        Sub_total = self.get_sub_total_concept(data_element)

        return {
            "Clave de producto o servicio.": ClaveProdServ,
            "Concepto": Descripcion,
            "Importe": Importe,
            "Sub total": Descuento,
            "Sub total": Sub_total,
        }

    def set_clave_prod_serv(self, data_element: dict):
        if data_element["ClaveProdServ"]:
            return data_element["ClaveProdServ"]
        return None

    def get_invoice_concept(self,  data_element: dict) -> str:
        return data_element.get("Descripcion")

    def get_Importe(self, data_element: dict) -> str:
        return data_element.get("Importe")

    def get_sub_total_concept(self,  data_element: dict) -> float:
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
        try:
            Impuestos = self.root.find(f"{self.__URL_CFDI__}Impuestos")
            if not Impuestos:
                return None

            Retenciones = Impuestos.find(f"{self.__URL_CFDI__}Retenciones")

            if not Retenciones:
                return None

            elements = self.get_childs(Retenciones)
            data_elements = list(map(self.get_items, list(elements.values())))
            return {obj["Impuesto"]: float(obj["Importe"]) for obj in data_elements}

        except KeyError or AttributeError:
            print(F"ERROR: get_retenciones -> {self.get_retenciones()}")
            return None

    def search_tag(self, name_tag: str, element: ET.Element):
        try:
            return lambda URL: next(
                filter(
                    lambda e: e.tag == f"{URL}{name_tag}", element.iter()
                )
            )
        except StopIteration:
            return None

    def get_traslado(self) -> dict[str]:
        try:

            Impuestos = self.root.find(f"{self.__URL_CFDI__}Impuestos")

            if not Impuestos:
                return None

            Traslados = Impuestos.find(f"{self.__URL_CFDI__}Traslados")
            Traslado = self.get_childs(Traslados)

            Retencion = map(self.get_items, list(Traslado.values()))
            return sum(float(objeto["Importe"]) for objeto in Retencion)

        except KeyError or AttributeError:
            print(F"ERROR: get_traslado -> {self.get_retenciones()}")
            return None

        except StopIteration:
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

    def searh_in_complement(self, name_tag: str):
        try:
            child_root = self.get_items(self.get_childs(self.root))
            child_complemento = self.root.find(
                f"{self.__URL_CFDI__}Complemento")
            return name_tag in child_complemento

        except (AttributeError, KeyError):
            return False

    def get_data_nominas(self):
        """Descripcion : Metodo que nos permite obtener los impuestos o deducciones que se le realizan a la nomina en cada una de las operaciones

        Return (Tuple[ ISR : str, IMSS : str])

        """

        Impuestos = {}
        def get_data(e): return self.get_items(self.get_childs(e))
        try:

            Complemento = get_data(self.root)["Complemento"]
            concept_complemento = get_data(Complemento)
            Data_nomina = get_data(concept_complemento["Nomina"])
            Deducciones = get_data(Data_nomina["Deducciones"])

            data_deducciones = list(
                map(self.get_items, list(Deducciones.values()))
            )
            Impuestos = {Deducion["TipoDeduccion"]: Deducion["Importe"]
                         for Deducion in data_deducciones}

            ISR = Impuestos.pop("002")
            Descuentos_deducciones = reduce(
                lambda acc, current: acc + current, map(float, Impuestos.values()))
        except AttributeError:
            return None
        except TypeError:
            Descuentos_deducciones = 0
        return ISR, Descuentos_deducciones

    def get_folio_relaciones(self):
        """Desccripcion : Metodo que nos permite obtener el folio relacionado de un CFDI para asi saber cual es el estado del mismo

        Return (str | None) : retorna un folio fiscal o NONE dependiento si existe o no
        """
        try:
            folio = next(
                filter(
                    lambda element: element.tag == "{http://www.sat.gob.mx/Pagos}DoctoRelacionado" or element.tag == f"{self.__URL_CFDI__}CfdiRelacionado", self.root.iter()
                )
            )
            folio_relacionado = folio.get("IdDocumento") or folio.get("UUID")
            return folio_relacionado
        except StopIteration:
            return None

    def _Element_Impuestos_locales_(self):
        """Descripcion : Metodo que me permite validar si existe un elemento de impuestos locales y envace a si si o no poder procesar este mismo para retorna ele elemento en si

        Returns:
            Element.Element: Elemento de la clase element que es una fraccion de un archivo XML
        """
        #
        return maybe.unit_maybe(f"{self.__URL_IMPUESTO_LOCAL__}ImpuestosLocales")\
            .bind(
            lambda url_xml : filter(
                lambda element_xml : element_xml.tag == url_xml,
                self.root.iter()
            ))\
            .bind(list)\
            .bind(lambda elemnt_list: elemnt_list[0] if list(elemnt_list) else None).value
        
    def Impuestos_locales(self):
        """Descripcion : metodo que me permite obtener los impuestos locales que pudieran exstir dentro de una factura

        Returns:
            float: es el monto de los impuestos acreditables que nos podrian cobrar por algun servicio o producto
        """
        return maybe.unit_maybe(self._Element_Impuestos_locales_())\
            .bind(lambda element : element.get("TotaldeTraslados"))\
            .value
        
        




if __name__ == '__main__':

    RFC = "PPR0610168Z1"
    problemas_descuento = "C:/Users/User/Documents/Rigo/2023/XML/Emitidas/Febrero/Febrero/0B8B6950-EAB0-4DA2-B14A-B09B6DB8846E.xml"
    path_recibidas = "C:/Users/User/Documents/Rigo/2023/XML/Recibidas/Febrero/Febrero/"
    
    Hospedaje_file = "0A310817-8381-439E-B278-AD69F9ED8C80.xml"
    path_hospedaje = f"{path_recibidas}/{Hospedaje_file}"
    cfdi = CFDI(f"{path_hospedaje}", RFC)

    data = cfdi.main()
    for key, value in data.items():
        print(
            f"""
        {key} : {value}""")
    cfdi.Impuestos_locales()