from typing import Optional, Union
import xml.etree.cElementTree as ET
import copy as c
import os

RFC = "PPR0610168Z1"    

class Maybe():
    def __init__(self, value) -> None:
        self.value = value

    
    def bind(self, func):
        if self.value is not None :
            return Maybe(func(self.value ))
        else: 
            return Maybe(None)


def unit_maybe(value):
    return Maybe(value)

def foreach(func : callable, list : list):
    for i in range(len(list)):
        func(list[i])
        

def get_value_in_list(list : list[str] ,string_in_list : str):
    return unit_maybe(list)\
            .bind(lambda list: next(
                filter(
                    lambda element : string_in_list in element, 
                    list
                ), None))\
            .bind(lambda url : "{"+url+"}")\
            .value


class Reed_xml():
    def __init__(self, path_document : str) -> None:
        if not self.validate_path(path_document): 
            raise ValueError("La ruta especificada no es válida.")
        
        self.xml = path_document
        self.tree = ET.parse(self.xml)
        self.root = self.tree.getroot()
        self.__set__url_CFDI__()
    
    def main(self):
        return self.get_obj_childs(self.root)
    
    def __set__url_CFDI__(self):
        try :
            schema = next(filter(lambda keys : "schemaLocation" in  keys, self.root.attrib.keys()))
            urls = list(filter( lambda string : string != " " , self.root.get(schema).split(" ")))

        except StopIteration:
            schema = None
    
        self.__URL_CFDI__ = get_value_in_list(urls, "http://www.sat.gob.mx/cfd/")
        
        self.__URL_IMPUESTO_LOCAL__ = get_value_in_list(urls, "implocal")

        self.__URL_NOMINA__ = get_value_in_list(urls, "http://www.sat.gob.mx/nomina" )

        # print(self.__URL_NOMINA__, self.__URL_CFDI__, self.__URL_IMPUESTO_LOCAL__)

    
    
    def validate_path(self, path: str):
        return os.path.exists(path)
    
    
    def get_keys(self, element : ET.Element):
        """Description obten las kyes de un elemento de un xml

        Params:
            - element (ET.Element): Es el elemento del cual quieres extraer las claves de sus propiedades

        Returnn list : retorna una lista con las keys del elemento
        """
        return element.keys()
        
    
    def get_values(self, element : ET.Element) -> list:
        """descripcion : metodo que nos otorga los valores de los atributos de un elemento xml

        Params:
            element (ET.Element): Es el elemento de un xml del cual se le extraeran sus valores de los atributos

        Returns:
            list: lista de datos con todos los valores de los atributos
        """
        return list(map(element.get, element.keys()))
    
    
    def get_items(self, element : ET.Element, condition : Optional[Union[str, int, bool]] = None) -> dict[str : str]:
        """descripcion : metodo que nos permite obtener los nombre y valores del conjunto de atributos que tiene un elemento xml
        
        Params:
            - element (ET.Element): elemento al cual se le extraeran los datos
            - condition (str | int | bool) condicion la cual sera aplicada a los nombre de los atributos
        
        Return (dict) : diccionario con los datos de los nombre y valores de los atributos de un elemento xml
        """
        keys = self.get_keys(element)
        values = self.get_values(element)
        return {key: value for key, value in zip(keys, values) if key != condition}
    
    
    def get_name_child_tags(self, element : ET.Element) -> list[str]:
        """descripcion : metodo que nos proporciona los tags (nombres) de los elementos hijo 

        Args:
            element (ET.Element): elemento del cual se extraeran los tag (nombre) de los hijos 

        Returns (list) : lista con todos los nombre de los hijos
        """
        conjunto_tags = {}
        
        def get_names_tag(element : ET.Element):
            
            tag = self.get_name_tag(element)
        
            if tag not in conjunto_tags:
                conjunto_tags[tag] = 1
                return tag
        
            conjunto_tags[tag] += 1
            return f"{tag} {conjunto_tags[tag]}"
        
        return list(map(get_names_tag, element))
        

    def get_obj_childs(self, element : ET.Element):
        """descripcion : Metodo que nos retorna una lista con los objetos hijos de un elemento

        Params:
            - element (ET.Element): Elemento del cual se extraen los hijos

        Return (list) : lista de objetos con los hijos de un elemento 
        """
        return list(map(lambda e : e, element))
    
        
    def get_childs(self, element : ET.Element) -> dict[str : ET.Element]:
        """descripcion : metodo que nos permite obtener los hijos de un elemento relacionados con tu name tag

        Args:
            element (ET.Element): elemento del cual se extraeran los hijos (objetos)

        Returns:
            dict[str : ET.Element]: dicc el cual tiene los hijos los hijos de un elemento relacionados con tu name tag
        """
        child_tags = self.get_name_child_tags(element)
        child_objs = self.get_obj_childs(element)
        return {key: value for key, value in zip(child_tags, child_objs)}
    
    
    
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

        
    def get_file_name(self) -> str:
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
        
        
    def get_element(self,element_xml : ET.Element, name_tag : str, url : str = None):
        """Description : Metodo que te permite buscar un elemento xml dentro de otro

        Args:
            element_xml (ET.Element): Es el elemento xml donde quiere buscar otro elemento xml
            name_tag (str): es ele nombre de la etiqueta xml que necesitas buscar
            url (str) : url que se tomara como espacio de nombre para la busqueda del elemento

        Returns:
            ET.Element: un elemento xml en caso de que si se encontro o None
        """
        tag_url = url or element_xml.tag.split('}')[0] + '}'
        return unit_maybe(f"{tag_url}{name_tag}")\
            .bind(element_xml.find)\
            .value
    
if __name__ == "__main__":
    pass