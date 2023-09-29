from app_cfdi.Impuestos.impuestos import Impuestos
from app_cfdi.Impuestos.impuestos_locales import Impuestos_locales
from app_cfdi.Nomina.Nomina import Nominas
from reed_xml import Reed_xml
from app_cfdi.Fechas.Fecha import Fechas_xml



class CFDI(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)
        
    def __str__(self) -> str:
        return f"""
    path : {self.xml}
    root : {self.root}
    """
    
    def get_data_cfdi():
        return {
            "Fecha en el estado de cuenta.": None,
            "Fecha de facturación.": None,
            "Tipo.": None,
            "Clase.": None,
            "Clave de producto o servicio.": None,
            "num": None,
            "Folio fiscal.": None,
            "Nombre.": None,
            "Concepto.": None,
        }