from utils import maybe
from utils import utils
from reed_xml import Reed_xml
import xml.etree.cElementTree as ET

class Nominas(Reed_xml):
    
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
        self.Nomina = self.__get_elements_nomina__()

    def __get_elements_nomina__(self) -> ET.Element | None:
        return maybe.unit_maybe(self.root)\
            .bind(lambda root_element : self.get_element(root_element, "Complemento"))\
            .bind(lambda elemnt_xml_complemento : self.get_element(elemnt_xml_complemento, "Nomina", self.__URL_NOMINA__))\
            .value
    

    def get_nomina_percepciones(self) -> dict[str] | None:
        return maybe.unit_maybe(self.Nomina)\
            .bind(lambda element_xml_nomina : self.get_element(element_xml_nomina, "Percepciones"))\
            .bind(lambda element_xml_percepciones : {
                "Importe sueldo" : element_xml_percepciones.get("TotalSueldos"),
                "Importe exento" : element_xml_percepciones.get("TotalExento"),
                "Importe Gravado" : element_xml_percepciones.get("TotalGravado")
                } 
            )\
            .value
    

    def get_nomina_deducciones(self) -> dict[str : str] | None:

        #obtenemos el elemento Deducciones del xml
        def get_deducciones_element(xml_nomina):
            return self.get_element(xml_nomina, "Deducciones")

        # funcion que me permite obtener los objetos hijos de un elemento xml.
        def get_child_elements(xml_element):
            return self.get_childs(xml_element).values()

        # funcion que me permite obtener los atributos de un elemento xml.
        def get_deduccion_items(xml_element):
            return self.get_items(xml_element)

        # funcion que mapea un conjunto de elementos xml para obtener sus atributos.
        def map_deduccion_items(xml_elements):
            return map(get_deduccion_items, xml_elements)

        return maybe.unit_maybe(self.Nomina) \
            .bind(get_deducciones_element) \
            .bind(get_child_elements) \
            .bind(list) \
            .bind(map_deduccion_items) \
            .bind(lambda deducciones: utils.transform_list_in_short_dictionary(
                deducciones, "Concepto", "Importe"
            )) \
            .value
    

    def get_importes_nominas(self) :
        persepciones = self.get_nomina_percepciones()
        deducciones = self.get_nomina_deducciones()
        persepciones.update(deducciones)
        print(persepciones)