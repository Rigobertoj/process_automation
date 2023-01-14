from functools import reduce
acreditante_1 = {'RFC': 'RARC860607497', 'Nombres': 'CARLOS MANUEL', 'ApellidoPaterno': 'RAMIREZ', 'ApellidoMaterno': 'ROSALES', 'FechaNacimiento': 20141127, 'Direccion': 'SANTA TERESA DE JESUS 266', 'ColoniaPoblacional': 'CAMINO REAL', 'DelegacionMunicipio': 'ZAPOPAN', 'Ciudad': 'ZAPOPAN', 'Estado': 'JALISCO', 'CP': 45040, 'NombreEmpresa': 'CARLOS MANUEL RAMIREZ ROSALES', 'Direccion E': 'SANTA TERESA DE JESUS 266', 'ColoniaPoblacion E': 'CAMINO REAL', 'DelegacionMunicipal E': 'ZAPOPAN', 'Ciudad E': 'ZAPOPAN', 'Estado E': 
'JALISCO', 'CP E': 45040, 'ClaveActualOtorgante': None, 'NombreOtorgante': None, 'CuentaActual': None, 'TipoResponsabilidad': 'I', 'TipoCuenta': 'P', 'TipoContrato': 'AR', 'ClaveUnidadMonetaria': 'MX', 'FrecuenciaPagos': 'M', 'MontoPagar': 80000, 'FechaAperturaCuenta': 20211206, 'FechaUltimoPago': 20220825, 'FechaUltimaCompra': 20211206, 'FechaCorte': 20230113, 'CreditoMaximo': 2000000, 'SaldoActual\xa0': 2000000, 'Limite credito': None, 'SaldoVencido': 583878.5893709798, 'PagoActual': 7, 'FechaPrimerIncumplimiento': 20220306, 'SaldoInsoluto': 2000000, 'MontoUltimoPago': 28501.87, 'PlazoMeses': 24, 'MontoCreditoOriginacion': 2000000}
        
class Persona():
    """
    Description : clase que nos permite modelar la estructura de los datos de un acreditante en etiquetas XML 
    
    ! TODA LA INFORMACION DEBE DE ESTAR EN MAYUSCULAS !
    
    Ejemplo :
        Nombre = {
            "RFC" : "CELA750508122",
            "PRIMER NOMBRE" : "ARACELI",
            "SEGUNDO NOMBRE" : "",
            "APELLIDO PATERNO" : "CERVANTES",
            "APELLIDO MATERNO" : "LUNA",
            "FECHA DE NACIMIENTO" : "19750508"
        }
        
    """
    def __init__(self,data_acreditante : dict):
        self.data_acreditante = data_acreditante
        self.__set_list_tag__(data_acreditante)
        
    
    def __set_list_tag__(self, data_acreditante : dict):
        """descripcion : Metodo nos establece las distintas lista con las claves (de un diccionario) que se deben de validar en la creacion de cada una de la etiquetas de 

        Params :
            data_acreditante (dict): diccionaraio con todos los datos minimos requeridos de un acreditado provenientes del excel 
        """
        list_keys_data_acreditante = list(data_acreditante.keys())
        self.list_data_creditor_keys_name  = list_keys_data_acreditante[:5]
        self.list_data_creditor_keys_Domicilio = list_keys_data_acreditante[5:11]
        self.list_data_creditor_keys_job = list_keys_data_acreditante[11:18]
        self.list_data_creditor_keys_acount = list_keys_data_acreditante[18:]
        
        
    def Create_element(self, elemnt_data: dict, name_tag: str):
        """
        Descripcion : Metodo que nos permite la creacion de un elemento con name_tag el cual contiene N cantidad de hijos los cuales estan contenidos en la clave y valor de el paramtro elemnt_data
        
        Example :
            <name_tag>
                <element_data.key>element_data.value</element_data.key>
            <name_tag>
            
        params : 
            - name_tag : nombre de la etique que retorna el metodo
            - elemnt_data (dict) : diccionario con los datos de los elementos hijo de la etique
        """
    
        Indentacion = "             "
        encabezado_data = list(
            map(lambda key, value : f"{Indentacion}<{key}>{value}</{key}>\n", elemnt_data.keys(), elemnt_data.values())
            )
    
        tags_elemsnt = reduce(lambda acum, data : acum + data, encabezado_data)    
        return f"""
        <{name_tag}>
        
{tags_elemsnt}
        </{name_tag}>
        """

    
    def __data_validate__(self, list_validaciones : list[str], nota = " "):
        """
        Descripcion : Metodo que nos permite validar los datos de un acreditante en etiquetas XML
        En si lo que hace es que  
        
        params : 
            - list_validaciones (list[str]) : lista con los nombres de las validaciones
        """
        data_acreditante = self.data_acreditante
                
        element_data = {}
        for value in list_validaciones:
            if value in data_acreditante:
                element_data[value] = data_acreditante[value]
            else :
                error = f"Revisa los campos pueden estar mal escritos o faltantes en la seccion {nota}"
                raise  KeyError(error)
        return element_data
    
    
    def Persona(self):
        """
        Descripcion : Metodo que se llama una ves que se halla contruido todo el objeto persona
        """
        self.Tag_Nombre = self.Nombre()
        self.Tag_Domicilio = self.Domicilios()
        self.Tag_Empleos = self.Empleos()
        self.Tag_Cuenta = self.Cuenta()
        return f"""
    <Persona>
        {self.Tag_Nombre}
        {self.Tag_Domicilio}
        {self.Tag_Empleos}
        {self.Tag_Cuenta}
    </Persona>
            """
    
    
    def Nombre(self): 
        """
        Descripcion : Metodo que nos permite crear el elemento <Nombre> de un acreditado en formato XML para su integracion en el XML principal
        
        params : 
            - None
            
        return (str) : etiqueta <Nombre> con todos los datos ya validados  
        """
        Name_tag = "Nombre"
         
        element_data = self.__data_validate__(self.list_data_creditor_keys_name, f"<{Name_tag}>")
        tag_nombre = self.Create_element(element_data, Name_tag)   
        
        return tag_nombre
        
        
    def Domicilio(self):
        Name_tag = "Domicilio"
        
        element_data = self.__data_validate__(self.list_data_creditor_keys_Domicilio, f"<{Name_tag}>")
        tag_domicilio = self.Create_element(element_data, Name_tag)
        
        return tag_domicilio
        
        


    def Domicilios(self):
        Domicilio = self.Domicilio()
        return f"""
    <Domicilios>
        {Domicilio}
    </Domicilios>
        """
        
    
    
    def Empleo(self):
        Name_tag = "Empleo"
        
        element_data = self.__data_validate__(self.list_data_creditor_keys_job, f"<{Name_tag}>")
        
            
        
        # TODO : re estrucutracion 
        # data_clen_part_1 = list(map(lambda key: key[:-2] , filter(lambda  key : "E" in key[-2:], list(element_data.keys()))))
        
        # data_clen_part_2 = list(filter(lambda key: "E" not in key[-2:], list(element_data.keys())))
        # print(data_clen_part_1)
        # print(data_clen_part_2)
        # data_clean = data_clen_part_2.append(data_clen_part_1)
        # print(data_clean)
        # data_element = {key : value for key, value in zip(data_clean, list(element_data.values()))}
        
        # print(list(data_element))    
        
        # element_data_2 = {key_ : value for key_, value in element_data.items() if "E" in key_[-2:]}
        # print(element_data_2)
        
        # TODO : re estructuracion funcional 
        for key in list(element_data.keys()):
            if "E" in key[-2:]:
                current_value_key = element_data[key]
                new_key = key[:-2]
                del element_data[key]
                element_data[new_key] = current_value_key
                        
        # print(element_data.keys()) 
        tag_empleo = self.Create_element(element_data, Name_tag)
        return tag_empleo
        

    def Empleos(self):
        tag_empleo = self.Empleo()
        return f"""
    <Empleos>
        {tag_empleo}
    </Empleos>
    """
    
    
    def Cuenta(self):
        Name_tag = "Cuenta"
        
        element_data = self.__data_validate__(self.list_data_creditor_keys_acount, f"<{Name_tag}>")
        tag_cuenta = self.Create_element(element_data, Name_tag)
        
        return tag_cuenta
        
        
if __name__ == "__main__":
    acreditante = Persona(acreditante_1)
    print(acreditante.Persona())