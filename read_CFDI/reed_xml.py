"""
En este script lo que queremos es obtener una serie de valores 
- fecha de factura : 
- Num clave del producto 
- folio fiscal (este esta en el titulo de documento)
- nombre del emisor : root[0].attrib["Nombre"]
- concepto
- subtotal
- impuestos
    - IVA : root_CFDI[2][0][0][0][0].attrib["TasaOCuota"]
    - Ret IVA 
    - Ret ISR 
- Total


CFDI = {

}

"""
import xml.etree.cElementTree as ET
import copy as c

CFDI_TASA_0 = "./CFDI/7513B197-3F46-4807-B4E6-1001AAA07248.xml"

class reed_xml :
    """
    Descripcion : 

    Params :

    return : 
        CFDI = {
            Fecha : str | Date, 
            Folio_fiscal : str,
            Personas : {
                "Emisor" : {
                    "Emisor_RFC": str,
                    "Emisor_name" : str
                },
                "Receptor" : {
                    "Receptor_RFC" : str,
                    "Receptor_name" : str
                }
            },
            Clave_producto : str
            mounts : [
                {
                    
                }
            ]
        }
            
    
    """
    CFDI = {}
    def __init__(self, path_document : str, nombre = " ") -> None:
        self.xml = path_document


    def get_data (self) -> dict:
        """

        
        """
        folio_fiscal = self.get_tax_folio(self.xml)

        self.tree = ET.parse(self.xml)
        self.root = self.tree.getroot()
            
        fecha = self.get_date_bill(root=self.root)
        self.CFDI["Fecha"] = fecha

        self.CFDI["Folio_fiscal"] = folio_fiscal

        person = self.get_names(root= self.root)
        self.CFDI["Personas"] = person

        clave_Produc_serv = self.get_clave_producto(root=self.root )

        self.CFDI["clave_Produc_serv"] = clave_Produc_serv

        self.get_concept(root=self.root)
        # self.get_mount(root=self.root)

        


        return self.CFDI


    def get_tax_folio (self, xml: str) -> str:
        """
        description : function thats return a tax folio

        params :

        return (str)  : tax folio

        """
        with open(xml) as xml :
            data = xml.name
            #obtenemos el ultimo elemento de la lista pues ahi esta el folio
            folio = data.split("/")[-1]

            # retiramos la extencion .xml que coforma los ultimos 4 caracteres
            return folio[:-4]
            


    def get_names(self, root : ET.Element) -> dict:
        Emisor_RFC = root[0].attrib["Rfc"]
        Emisor_name = root[0].attrib["Nombre"],
        Receptor_RFC = root[1].attrib["Rfc"]
        Receptor_name = root[1].attrib["Nombre"]

        return {
            "Emisor" : {
                "Emisor_RFC": Emisor_RFC,
                "Emisor_name" : Emisor_name
            },
            "Receptor" : {
                "Receptor_RFC" : Receptor_RFC,
                "Receptor_name" : Receptor_name
            }
        }


    def get_date_bill (self, root : ET.Element):
        return root.attrib["Fecha"]


    def get_clave_producto(self, root : ET.Element):
        """
        return : retorna la clave del producto o servicio
        """
        return root[2][0].attrib["ClaveProdServ"]
        
    
    def get_concept(self, root : ET.Element):
        products_servs = self.root[2]
        products_servs_copy = c.copy(products_servs)

        Conceptos = []
        for producto_servi in products_servs_copy:
            producto_servi.attrib.pop("NoIdentificacion")
            producto_servi.attrib.pop("ClaveUnidad")
            producto_servi.attrib.pop("Unidad")

            Conceptos.append(producto_servi.attrib)
        
        for concepto in Conceptos:
            print(concepto)
        
        return Conceptos
    def get_taxes(): 
        pass

    def get_mount(self, root : ET.Element):
        #obtenemos los productos o servicios
        products_servs = self.root[2]
        
        sub_totales = []
        impuestos = {
            "IVA": [],
            "Ret. IVA" : [],
            "Ret. ISR" : [],
            "IEPS" : []
        }
        for producto_servi in products_servs:
            print(producto_servi.attrib[0][0][0])




if __name__ == "__main__":
    DATA = reed_xml(CFDI_TASA_0)
    print(DATA.get_data())