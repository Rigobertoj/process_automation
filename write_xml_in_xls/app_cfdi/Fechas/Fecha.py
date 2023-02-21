from utils import maybe
from utils import utils
from reed_xml import Reed_xml
import xml.etree.cElementTree as ET
from datetime import datetime


class Fechas_xml(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
        
    def convert_type_time(self, time_string: str):
        return datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S")

    def fecha_facturacion(self):
        def get_items_certificado(element : ET.Element):
            return self.get_items(element, "Certificado")
        
        return maybe.unit_maybe(self.root)\
            .bind(get_items_certificado)\
            .bind(lambda element_xml_certificado : element_xml_certificado.get("Fecha"))\
            .value
