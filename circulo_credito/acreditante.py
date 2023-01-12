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
        data_acreditante = self.data_acreditante
        
        if nota == "<Empleo>": 
            print(data_acreditante)

        
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