from utils import maybe
from utils import utils
from reed_xml import Reed_xml
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
        
        
    def get_atributes_taxes_element(self, type : str):
        """Description : metodo que nos permite obtener los atributos de un elemento xm, sobre el importe del pago de impuestos 

        Args:
            type (str): Nombre del elemento xml al cual se le extrera la informacion

        Returns:
            dict[str: float ]: diccionario con los datos del importe de un tipo de impuesto
        """
        # bind 1 : obtenemos el elemento xml
        # bind 2 : obtenemos los hijos del elemento xml
        # bind 3 : mapeamos los objetos de la clase ET.Element para obtener sus atributos 
        return maybe.unit_maybe(type)\
            .bind(self.get_element_in_taxes)\
            .bind(self.get_childs)\
            .bind(lambda child_element : list(map(self.get_items, list(child_element.values()))))\
            .value

    def get_data_taxes(self, type):
        """Description : metodo que nos permite cambiar la estructura de los datos que nos retorna un elemenento xml de sus atributos
        
        params 
            - type (str) : Nombre del elemento xml al cual se le extrera la informacion y se restructurara la misma

        return (dict) : retorna un diccionario con los elementos comprimidos en una clave, Impuesto y un value, Importe
        """
        data_child_attributes = self.get_atributes_taxes_element(type)

        return  maybe.unit_maybe(data_child_attributes)\
            .bind(lambda data_attr : utils.tranform_list_in_short_diccionary(data_attr, "Impuesto", "Importe"))\
            .value

    
    def get_taxes(self):
        """Descripcion : metodo que nos permite obtener de manera estructurada los impuestos de la factura

        Returns:
            Tupla[int | None, int | None, int | None]: Retornamos una tupla con los valores del IVA, Ret de IVA y Ret de ISR en ese orden
        """

        traslado = self.get_data_taxes("Traslados") or {}
        
        ret = self.get_data_taxes("Retenciones") or {}

        return traslado.get("002"), ret.get("002"), ret.get("001"),
