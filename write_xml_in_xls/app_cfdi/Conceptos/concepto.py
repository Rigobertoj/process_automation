from utils import maybe
from utils import utils
from reed_xml import Reed_xml
import xml.etree.cElementTree as ET
from datetime import datetime


class Concepto(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
        
    def get_concepto_atributos(self, element : ET.Element):
        self.concepto = self.get_items(element)
        

class Descripcion(Concepto):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
    
    def get_descripccion_producto(self, element : ET.Element):
        return maybe.unit_maybe(element)\
            .bind(self.get_concepto_atributos)\
            .bind(lambda obj : obj.get("Descripcion"))\
            .value

class Clave_producto_servicio(Concepto):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
    
    def get_clave_producto_serv():
        pass
    
class Importe_concepto(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)