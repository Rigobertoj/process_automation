from ..utils import maybe
from ..utils import utils
from ..reed_xml import Reed_xml
import xml.etree.cElementTree as ET


class Impuestos(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
    
    
    def get_element_in_taxes(self, name_tag_element_xml) -> ET.Element | None:
        """Description : metodo que nos permite buscar un elemento dentro de la seccion de impuestos

        Args:
            name_tag_element_xml (str): Nombre del elemento que queremos buscar en la seccion de impuestos en el elemento

        Returns:
            (ET.Element) | None : retorna el elemento xml si es que lo encontro
        """
        element_taxes = self.get_element(self.root, "Impuestos")
        return maybe.unit_maybe(element_taxes)\
            .bind(
                lambda element_xml : self.get_element(element_xml, name_tag_element_xml)
                )\
            .value
        
        
    def get_data_taxes(self, type):
        """Description : metodo que nos permite obtener los datos de un elemento xml sobre el importe del pago de impuestos 

        Args:
            type (str): Nombre del elemento xml al cual se le extrera la informacion

        Returns:
            dict[str: float ]: diccionario con los datos del importe de un tipo de impuesto
        """
        #obtenemos el elemento xml
        element = self.get_element_in_taxes(type)
        #obtenemos los hijos del elemento xml
        child_element = self.get_childs(element)
        #mapeamos los objetos de la clase ET.Element para obtener sus atributos
        data_child = list(map(self.get_items, list(child_element.values())))
        # extraemos solo los datos del tipo de impuesto y el importe
        

        new_obj = {
            f"{obj['Impuesto']} {index}" if obj['Impuesto'] in new_obj else obj['Impuesto']: obj['Importe'] 
            for index, obj in enumerate(data_child)
            }
                
        return new_obj
    
        
    def get_taxes(self):
        """Descripcion : metodo que nos permite obtener de manera estructurada los impuestos de la factura

        Returns:
            Tupla[int | None, int | None, int | None]: Retornamos una tupla con los valores del IVA, Ret de IVA y Ret de ISR en ese orden
        """

        traslado = self.get_data_taxes("Traslados") or {}
        
        ret = self.get_data_taxes("Retenciones") or {}

        return traslado.get("002"), ret.get("002"), ret.get("001"),


class Impuestos_locales(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)


    def _element_Impuestos_locales_(self):
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

    def impuestos_locales_acre_tras(self, type : str ):
        """Descripcion : metodo que me permite obtener los impuestos locales que pudieran exstir dentro de una factura

        Params :
            - type (str) : es el tipo de impuesto si acreditable o trasladado
                - TotaldeTraslados
                - TotaldeRetenciones

        Returns:
            float: es el monto de los impuestos acreditables que nos podrian cobrar por algun servicio o producto
        """
        return maybe.unit_maybe(self._element_Impuestos_locales_())\
            .bind(lambda element : element.get(type))\
            .value

    def Impuestos_locales(self):
        """Description : Metodo que nos permite obtener los impuesto acreditables y traslados locales

        Returns:
            tupla[float, float]: es una tupla con los datos de los impuestos acreditables y trasladados locales
        """
        Acreditables = self.impuestos_locales_acre_tras("TotaldeTraslados")
        Trasladados = self.impuestos_locales_acre_tras("TotaldeRetenciones")
        return Acreditables, Trasladados