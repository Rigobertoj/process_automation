from functools import reduce
import xml.etree.cElementTree as ET
import copy as c
import os
import time
import sys


RFC = "PPR0610168Z1"
class reed_xml :
    """
    Descripcion : esta clase permite obtener a traves de un XML CFDI los datos de la misma factura asi como el dia de emision, los productos, la descripcion de los mismos, esto con el objetivo de brindas al desarrollador una mayor facilidad a la hora de extrar y analizar la informacion de un CFDI para su procesamiento.

    No todos lo datos retornados se deben de interpretar como str si no que la mayoria son o enteros o decimales pero por la naturaleza de un XML se extraen en formato str

    Params :

    return : 
        CFDI = {
            Tipo : str,
            Complemento : boold,
            Efecto_fiscal : str,
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
            Mount = {
                'SubTotal' : str,
                'Descuento' : str
                'Total' : str
            }

            Mount_prod_serv : [
                {
                   Concepto : {
                    'ClaveProdServ' : str,
                    'Cantidad' : str,
                    'ClaveUnidad' : str,
                    'Descripcion' : str,
                    'ValorUnitario' : str, 
                    'Importe' :str
                   },
                   Impuestos = {
                        'Acreditables' : {
                         'Base' : str, 
                         'Impuesto' : str, 
                         'TipoFactor' : str, 
                         'TasaOCuota' : str, 
                         'Importe' : str,
                        }, 
                        'Trasladados' : {
                             002 (IVA) : {
                                 'Base' : str, 
                                 'Impuesto' : str, 
                                 'TipoFactor' : str, 
                                 'TasaOCuota' : str,
                                 'Importe' : str
                             },
                             001 (ISR) : {
                                 'Base' : str, 
                                 'Impuesto' : str, 
                                 'TipoFactor' : str, 
                                 'TasaOCuota' : str,
                                 'Importe' : str
                             }
                        },
                    }
                }
            ]
        }
            
    
    """
    __CFDI = {}
    def __init__(self, path_document : str, RFC : str, nombre = " ", ) -> None:
        self.xml = path_document
        self.__RFC = RFC.upper()
        self.tree = ET.parse(self.xml)
        self.root = self.tree.getroot()
        #TODO : Crear un atributo que atravez de un metodo(o funcion) me permita validad el tipo de CFDI que se ingresa y asi procesarlo de la manera mas adecuada
        self.type = str


    def get_tag(self,name_tag: str) -> ET.Element:
        """
        descripcion : metodo que nos permite encontrar y retornar algun elemento a travez del nombre de su etiqueta

        params :
            - root (ET.Element) : root es la raiz del CFDI
            - name_tag (str) : nombre de la etiqueta
        
        return : retornar el objeto Element del CFDI 
        """
        # Define una función de filtro que compruebe si el nombre de la etiqueta sea el mismo que name_tag
        def es_emisor(tag):
            return self.get_name_tag(tag) == name_tag
    
        # Obtiene el primer elemento que cumpla la condición utilizando next()
        try:
            tag = filter(es_emisor, self.root.iter())
        except StopIteration:
            folio_fiscal = self.__CFDI["Folio_fiscal"]
            print(f"SpotIteration {folio_fiscal}")
            return StopIteration
        return tag


    def get_data (self) -> dict:
        """
        descripcion : metodo que nos permite obtener toda la informacion de un CFDI xml para su posterior procesado de esta manera podemos utilizar los dato del mismo de la manera que queramos

        return (dict) : este medoto retorna un diccionario por cada CFDI el cual viene identificadas las propiedades de la clase en la doc de la misma        
        """
        Tipo = self.get_tipo_CFDI()
        self.__CFDI["Tipo"] = Tipo
        #obtenemos el folio fiscal
        folio_fiscal = self.get_tax_folio()
        self.__CFDI["Folio fiscal"] = folio_fiscal

        fecha = self.get_date_bill()
        self.__CFDI["Fecha"] = fecha

        person = self.get_names()
        self.__CFDI["Personas"] = person

        self.__CFDI["Mount"] = self.get_mount()
        return self.__CFDI


    def get_tipo_CFDI(self):
        """
        Descripcion : metodo que nos permite definir si un CFDI fue emitido o recibido esto para efecto fiscales.

        params :
            - root (ET.Element) : root es la raiz del CFDI
            
        return (str) : retorna Recibido o Emitido
        """
        
        tag_Emisor = next(self.get_tag(self.root, 'Emisor'))
        Emisor = tag_Emisor.attrib
        if "Rfc" in Emisor:
            if Emisor["Rfc"] != self.__RFC:
                return "Recibido"
            else :
                return "Emitido"


    def get_tax_folio (self) -> str:
        """
        description : funcion que nos permite obtener el folio fiscal del documento CFDI

        params :
            - xml (str) : ruta donde se aloja el CFDI 

        return (str)  : folio fiscal

        """
        #abrimos el documento
        with open(self.xml) as xml:
            #obtenemos el nombre del archivo
            data = xml.name
            
            #obtenemos el ultimo elemento de la lista pues ahi esta el folio
            folio = data.split("/")[-1]

            # retiramos la extencion .xml que coforma los ultimos 4 caracteres
            return folio[:-4]
            


    def get_names(self) -> dict[dict[str, str], dict[str, str]]:
        """
        Descriptcion : Metodo que nos permite obtener los nombres de las personas involucradas en la prestacion de un bien o servicio en un objeto dict separadas dentro del mismo por dos dict el primero siendo el Emisor y el segundo siendo el Receptor 

        params : 
            - root (ET.Element) : root es la raiz del CFDI

        return dict[dict[str, str], dict[str, str]] : diccionario con el emisor y recepto en ese orden separador por dos diccionarios dentro del mismo 
        """
        #obtenemos los datos indexados 

        #datos del emisor que estan en primera posicion
        Emisor = next(self.get_tag(self.root, "Emisor"))
        Receptor = next(self.get_tag(self.root, "Receptor"))
        
        Emisor_RFC = Emisor.attrib["Rfc"]
        Emisor_name = Emisor.attrib["Nombre"]
        
        #datos del receptor que estan en la segunda posicion
        Receptor_RFC = Receptor.attrib["Rfc"]
        Receptor_name = Receptor.attrib["Nombre"]

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


    def get_date_bill (self) -> str:
        """
        Descripcion : Metodo que nos permite retornar la fecha de emicion del CFDI

        params :
            - root (ET.Element) : root es la raiz del CFDI

        return (str) : Retorna la fecha de emicion de la factura 

        """
        Comprobante = self.root.attrib
        if "Fecha" in Comprobante:
            return Comprobante["Fecha"]
        else:
            return None

            
    def get_concept(self) -> list[dict[str, str]]:
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
        Conceptos_product_serv = next(self.get_tag(self.root, "Conceptos"))

        #copeamos el objeto pues sera mutado
        products_servs_copy = c.copy(Conceptos_product_serv)
        
        #funcion que nos permite eleminar y retornar los conceptos que necesitemos
        def delete_attrib(Obj_concept : ET.Element):
            if "NoIdentificacion" in Obj_concept : Obj_concept.attrib.pop("NoIdentificacion")
            if "ClaveUnidad" in Obj_concept : Obj_concept.attrib.pop("ClaveUnidad")

            return Obj_concept.attrib

        # a traves de un mapeo eliminamos los atributos que no necesitamos
        Conceptos = list(
            map(
                delete_attrib,
                products_servs_copy
                )
            )
        return Conceptos


    def get_taxes_prod_serv(self, root : ET.Element):
        # TODO : changue the doc 
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
        # TODO : restructuracion del codigo
        #obtenemos el elemento cfdi:Conceptos
        Conceptos_product_serv = root[2]
        #copeamos el elemento pues sera mutado
        product_serv_copy = c.copy(Conceptos_product_serv)

        #indexamos el elemento para obtener el objeto (dict) con los atributos de los impuestos calculados
        for element in product_serv_copy.iter():
            if "Concepto" == self.get_name_tag(element):
                return element.attrib

        get_mounts = lambda element : element[0][0][0].attrib
        get_mounts_2 = filter(lambda tag : self.get_name_tag(tag) == 'Concepto', product_serv_copy.iter())
        #aplicamos la funcion anterios a la lista con los productos o servicios
        taxes = list(
            map(
                get_mounts, 
                product_serv_copy
            )
        )

        return taxes

    def get_name_tag(self, element_xml : ET.Element):
        """
        Descripcion : Metodo que nos prmite obtener el nombre de alguna etiqueta del CFDI: ejemplo :
            - {http://www.sat.gob.mx/cfd/3}Retenciones -> Retenciones

        Params : 
            element_xml (ET.Element) : Este es el elemento del cual quiere obtener su etiqueta o tag

        return (str) : Retorna el nombre de la etiqueda o tag del elemento introducido
        """
        tag = element_xml.tag.split("}")[1]
        return tag


    def get_Ret_taxes_prod_serv(self):
        """
        Descripccion : MEtodo que nos permite obtener las retenciones de un CFDI si este fuera algun pago por servicio profecional o alguna actividad a la cual se le hagan retenciones

        params :
            - root (ET.Element) :  root es la raiz del CFDI 

        return dict[dict, dict] : Un diccionario con 2 dentro de si los cuales tiene las retenciones o cuotas retenidad.

        """
        conceptos = self.get_tag(self.root, 'Conceptos')
        ret = {}
        i = 0
        for concepto in conceptos:
            if i > 0:
                break            
            i += 1
            for elements in concepto.iter():
                tag = self.get_name_tag(elements)
                if tag == "Retencion":
                    ret[elements.attrib["Impuesto"]] = elements.attrib
        
        return ret 
            

    def get_mount_prod_serv(self, root : ET.Element) -> list[dict[str, str]]:
        """
        Descripion : Metodo que nos permite obtener una lista de objeto los cueles tiene los montos de cada producto que se aquirio. 

        No todos lo objetos retornados se deben de interpretar como str si no que la mayoria son o enteros o decimales pero por la naturaleza de un XML se extraen en formato str

        params :
            - root (ET.Element) :  root es la raiz del CFDI
        
        return list[dict[str, str]] : una lista con los objetos con los datos de cada compra
        
        """
        #obtenemos los productos o servicios
        
        concepts = self.get_concept(root)

        #obtenemos los impuestos de dichos productos o servicios
        taxes = self.get_taxes_prod_serv(root)
        
        Retenciones = self.get_Ret_taxes_prod_serv(root)

        #contruimos un unico objeto con las los valores de ambos
        def contruc_item_produc_serv(concept : dict, taxe : dict):
            montos = {}
            
            tipo = self.get_tipo_CFDI(root)
            montos["Concepto"] = concept
            
            if tipo == "Recibido" :
                montos["Impuestos"] = { 
                    "Acreditables" : taxe 
                    }
                if not (not Retenciones):
                    montos["Impuestos"].update({"Trasladados" :Retenciones})
            else:
                montos["Impuestos"] = { 
                    "Trasladados" : Retenciones 
                    }
                if not (not taxe): 
                    montos["Impuestos"].update({"Acreditables" : Retenciones})

            return montos


        products_serv_mounts = list(
            #mapeamos a la lista de objetos (productos e impuestos) con la funcion anterios
            map(
                contruc_item_produc_serv,
                concepts,
                taxes
                )
            )

        return products_serv_mounts


    def get_mount(self):
        
        # TODO : Create the doc

        mounts = {}
        if 'SubTotal' in self.root.attrib : 
            mounts['SubTotal'] = float(self.root.attrib["SubTotal"])
        
        if 'Descuento' in self.root.attrib :
             mounts['Descuento'] = float(self.root.attrib['Descuento'])
        else :
            mounts['Descuento'] = 0

        if 'Total' in self.root.attrib :
            mounts['Total'] = float(self.root.attrib['Total'])
        
        taxes = self.get_taxes()
        if mounts is None :
            return 
        mounts.update(taxes)
        # print(mounts)
        return mounts


    def get_taxes(self):
        
        # TODO : Create the doc
        
        
        taxes = {}

        
        def Complemento():
            """
            descripcion : 
            
            """
            taxes = {
                'Traslado 16':0,
                'Traslado 0':0,
                'Retenciones':0
            }

        def filter_element_taxes(tag: ET.Element):
            if 'TotalImpuestosTrasladados' in tag.attrib  or 'TotalImpuestosRetenidos' in tag.attrib:
                return tag

            return taxes
        elements_impuestos = list(self.get_tag(self.root, 'Impuestos'))

        Impuestos = filter(filter_element_taxes, elements_impuestos)

        try :
            Impuestos = next(Impuestos)
        except StopIteration:
            return  Complemento()


        if Impuestos == StopIteration and self.get_tag(self.root, 'Complemento') is not None:
            return Complemento()       
        

        for impuesto in Impuestos.iter():
            if self.get_name_tag(impuesto) == "Traslado":
                if "Exento" in impuesto.attrib["TipoFactor"]:
                    return Complemento()
                    
                if '0.16' in impuesto.attrib["TasaOCuota"]:
                    taxes['Traslado 16'] = impuesto.attrib["Importe"]
                    
                else:
                    taxes['Traslado 0'] = impuesto.attrib["Importe"]
                    
            if self.get_name_tag(impuesto) == "Retencion":

                if "002" in impuesto.attrib["Impuesto"]:
                    taxes["Retenciones IVA"] = impuesto.attrib["Importe"]
                if "001" in impuesto.attrib["Impuesto"]:
                    taxes["Retenciones ISR  "] = impuesto.attrib["Importe"]
        
        return taxes
    

        
            


if __name__ == "__main__":
#CFDI_TASA_0 = "./CFDI/7513B197-3F46-4807-B4E6-1001AAA07248.xml"
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    produce_un_error_Complemente = "./CFDI/Testing_CFDI/056b1d70-7d25-45f6-bd5c-cdbe0adcf6f9.xml"
    produce_un_error = './CFDI/Testing_CFDI/052227d9-4d89-4438-b6c1-0dd183dfc4a1.xml'
    produce_un_error_fecha = "./CFDI/Testing_CFDI/02f933ce-1f0a-4628-920d-f5bb3ae4921f.xml"
    CFDI_HONORARIOS = "./CFDI/Testing_CFDI/4ABA0B0C-37D2-4127-9A43-B02C2432F392.xml" 
    Error_wb = './CFDI/Testing_CFDI/ff674a74-b484-4cf1-9685-b86f758c00c5.xml'
    NOMINA = './CFDI/Testing_CFDI/F3608EEE-5DEF-423E-BC6C-5C54616B49BD'
    DATA = reed_xml(produce_un_error_Complemente, RFC=RFC)
    data = DATA.get_data()
    print(DATA.get_mount())
    print(data)
    # dir_path = './CFDI/testing_CFDI'
    # xml = reed_multiples_xml(dir_path, RFC=RFC)

    # print(xml)