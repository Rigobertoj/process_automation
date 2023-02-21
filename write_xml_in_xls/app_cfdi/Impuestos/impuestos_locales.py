from utils import maybe
from utils import utils
from reed_xml import Reed_xml
import xml.etree.cElementTree as ET

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