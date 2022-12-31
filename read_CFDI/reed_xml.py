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
from    functools import reduce
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
        #obtenemos el folio fiscal
        folio_fiscal = self.get_tax_folio(self.xml)

        self.tree = ET.parse(self.xml)
        self.root = self.tree.getroot()
            
        fecha = self.get_date_bill(root=self.root)
        self.CFDI["Fecha"] = fecha

        self.CFDI["Folio_fiscal"] = folio_fiscal

        person = self.get_names(root= self.root)
        self.CFDI["Personas"] = person

        self.get_mount(self.root)


        return self.CFDI


    def get_tax_folio (self, xml: str) -> str:
        """
        description : funcion que nos permite obtener el folio fiscal del documento CFDI

        params :
            - xml (str) : ruta donde se aloja el CFDI 

        return (str)  : folio fiscal

        """

        #abrimos el documento
        with open(xml) as xml:
            #obtenemos el nombre del archivo
            data = xml.name
            
            #obtenemos el ultimo elemento de la lista pues ahi esta el folio
            folio = data.split("/")[-1]

            # retiramos la extencion .xml que coforma los ultimos 4 caracteres
            return folio[:-4]
            


    def get_names(self, root : ET.Element) -> dict[dict[str, str], dict[str, str]]:
        """
        Descriptcion : Metodo que nos permite obtener los nombres de las personas involucradas en la prestacion de un bien o servicio en un objeto dict separadas dentro del mismo por dos dict el primero siendo el Emisor y el segundo siendo el Receptor 

        params : 
            - root (ET.Element) : root es la raiz del CFDI

        return dict[dict[str, str], dict[str, str]] : diccionario con el emisor y recepto en ese orden separador por dos diccionarios dentro del mismo 
        """
        #obtenemos los datos indexados 

        #datos del emisor que estan en primera posicion
        Emisor_RFC = root[0].attrib["Rfc"]
        Emisor_name = root[0].attrib["Nombre"]
        
        #datos del receptor que estan en la segunda posicion
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


    def get_date_bill (self, root : ET.Element) -> list[dict[str, str]]:
        return root.attrib["Fecha"]

            
    def get_concept(self, root : ET.Element):
        """
        descripccion : metodo que nos permite obtener el objeto con los atributos de los conceptos descriptos en el CFDI asi obtenemos los datos como :
            - clave del producto 
            - Cantidad de unidades compradas de un producto
            - Descripcion (el concepto de la factura)
            - Valor unitarios
            - Importe 
            - Descuento

        params : 
            - root (ET.Element) : root es la raiz del CFDI 

        return list[dict[str, int]] : retorna una lista con los objetos que contiene los atributos de los conceptos de cada producto

        """

        #obtenemos el elemento cfdi:Conceptos
        Conceptos_product_serv = root[2]

        #copeamos el objeto pues sera mutado
        products_servs_copy = c.copy(Conceptos_product_serv)
        
        #funcion que nos permite eleminar y retornar los conceptos que necesitemos
        def delete_attrib(element_conceptos : ET.Element):
            element_conceptos.attrib.pop("NoIdentificacion")
            element_conceptos.attrib.pop("ClaveUnidad")
            element_conceptos.attrib.pop("Unidad")
            return element_conceptos.attrib

        # a traves de un mapeo eliminamos los atributos que no necesitamos
        Conceptos = list(
            map(
                delete_attrib,
                products_servs_copy
                )
            )
        
        return Conceptos
    
    
    def get_taxes(self, root : ET.Element):
        """
        Descripccion : Metodo que nos permite obtene el objeto con los atributos de los impuestos grabados a cada uno de los productos en la factura como :
            - Base  (Base grabable)
            - Impuesto (tipo)
            - Tasa factor (Tasa)
            - Tasa o cuota (porcentaje o monto)
            - importe (cantidad a pagar)

        Params :
            - root (ET.Element) :  root es la raiz del CFDI 


        Return list[dict[str, str]] : una lista con los objetos que contiene los atributos de los impuestos grabados a cada producto
        """
        #obtenemos el elemento cfdi:Conceptos
        Conceptos_product_serv = root[2]

        #copeamos el elemento pues sera mutado
        product_serv_copy = c.copy(Conceptos_product_serv)

        #indexamos el elemento para obtener el objeto (dict) con los atributos de los impuestos calculados
        get_mounts = lambda element : element[0][0][0].attrib
        
        #aplicamos la funcion anterios a la lista con los productos o servicios
        taxes = list(
            map(
                get_mounts, 
                product_serv_copy
            )
        )
        for taxe in taxes :
            print(taxe.values())
        return taxes
        

    
    def get_mount(self, root : ET.Element):
        """
        
        """
        #obtenemos los productos o servicios
        concepts = self.get_concept(root)

        #obtenemos los impuestos de dichos productos o servicios
        taxes = self.get_taxes(root)

        #contruimos un unico objeto con las los valores de ambos
        def contruc_item_produc_serv(concept : dict, taxe : dict):
            #actualizamos los elementos de concepts
            concept.update(taxe)
            #retornamos el nuevo objeto
            return concept


        products_serv_mounts = list(
            #mapeamos a la lista de objetos (productos e impuestos) con la funcion anterios
            map(
                contruc_item_produc_serv,
                concepts,
                taxes
                )
            )

        return products_serv_mounts




if __name__ == "__main__":
    DATA = reed_xml(CFDI_TASA_0)
    print(DATA.get_data())