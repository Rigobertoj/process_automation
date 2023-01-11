from functools import reduce
acreditante_1 = {'RFC': 'RARC860607497', 'PRIMER NOMBRE': 'CARLOS', 'SEGUNDO NOMBRE': 'MANUEL', 'APELLIDO PATERNO': 'RAMIREZ', 'APELLIDO MATERNO': 'ROSALES', 'FECHA DE NACIMIENTO': 20141127, 'CALLE': 'SANTA TERESA DE JESUS', 'NUMERO EXTERIOR': 266, 'NUMERO INTERIOR': None, 'COLONIA': 'CAMINO REAL', 'DELEGACION O MUNICIPIO': 'ZAPOPAN', 'CIUDAD': 'ZAPOPAN', 'ESTADO': 'JALISCO', 'CODIGO POSTAL': 45040, 'NOMBRE O RAZON SOCIAL': 'CARLOS MANUEL RAMIREZ ROSALES', 'DIRECCION': 'SANTA TERESA DE JESUS 266', 'COLONIA POBLACIONAL': 'CAMINO REAL', 'DELEGACION MUNICIPAL': 'ZAPOPAN', 'CIUDAD E': 'ZAPOPAN', 'ESTADO E': 'JALISCO', 'CP E': 45040, 'CLAVE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NOMBRE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NUMERO CREDITO VIGENTE': None, 'TIPO DE RESPONSABILIDAD': 'I', 'TIPO DE CREDITO ': 'P', 'TIPO DE PRODUCTO': 'AR', 'MONEDA': 'MX', 'FRECUENCIA DE PAGO': 'M', 'MONTO DE PAGO': 80000, 'FECHA DE APERTURA': 20211206, 'FECHA DE ULTIMO PAGO': 20220825, 'MONTO DEL CREDITO A LA ORIGINACION': 2000000, 'PLAZO EN MESES': 24, 'FECHA DE LA ULTIMA DISPOSICION O COMPRA': 20211206, 'FECHA DEL REPORTE ACTUALIZACION O CORTE': 20230113, 'CREDITO MAXIMO UTILIZADO': 2000000, 'SALDO ACTUAL': 2000000, 'SALDO VENCIDO ': 583878.5893709798, 'FORMA DE PAGO O PAGO ACTUAL': 7, 'FECHA DEL PRIMER INCUMPLIMIENTO': 20220306, 'SALDO INSOLUTO DEL PRINCIPAL': 2000000, 'MONTO DEL ULTIMO PAGO': 28501.87}
        
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
        
        list_validacion = ['RFC', 'PRIMER NOMBRE', 'SEGUNDO NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'FECHA DE NACIMIENTO']
        Name_tag = "Nombre"
         
        element_data = self.__data_validate__(list_validacion, f"<{Name_tag}>")
        tag_nombre = self.Create_element(element_data, Name_tag)   
        
        return tag_nombre
        
        
    def Domicilio(self):

        list_validacion = ['CALLE', 'NUMERO EXTERIOR', 'NUMERO INTERIOR', 'COLONIA', 'DELEGACION O MUNICIPIO', 'CIUDAD', 'ESTADO', 'CODIGO POSTAL']
        
        Name_tag = "Domicilio"
        element_data = self.__data_validate__(list_validacion, f"<{Name_tag}>")
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
        list_validacion = ['NOMBRE O RAZON SOCIAL', 'DIRECCION', 'COLONIA POBLACIONAL', 'DELEGACION MUNICIPAL', 'CIUDAD E', 'ESTADO E', 'CP E']
        Name_tag = "Empleo"
        element_data = self.__data_validate__(list_validacion, f"<{Name_tag}>")
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
        list_validacion = ['NOMBRE DEL USUARIO QUE REPORTA EL CREDITO', 'NUMERO CREDITO VIGENTE', 'TIPO DE RESPONSABILIDAD', 'TIPO DE CREDITO ', 'TIPO DE PRODUCTO', 'MONEDA', 'FRECUENCIA DE PAGO', 'MONTO DE PAGO', 'FECHA DE APERTURA', 'FECHA DE ULTIMO PAGO', 'MONTO DEL CREDITO A LA ORIGINACION', 'PLAZO EN MESES', 'FECHA DE LA ULTIMA DISPOSICION O COMPRA', 'FECHA DEL REPORTE ACTUALIZACION O CORTE', 'CREDITO MAXIMO UTILIZADO', 'SALDO ACTUAL', 'SALDO VENCIDO ', 'FORMA DE PAGO O PAGO ACTUAL', 'FECHA DEL PRIMER INCUMPLIMIENTO', 'SALDO INSOLUTO DEL PRINCIPAL', 'MONTO DEL ULTIMO PAGO']
        Name_tag = "Cuenta"
        element_data = self.__data_validate__(list_validacion, f"<{Name_tag}>")
        tag_cuenta = self.Create_element(element_data, Name_tag)
        return tag_cuenta
        
    
class circulo_credito(Persona):
    """
    Descripcion : Clase que nos proporciona una estructura definida de los parametros minimos requeridos para el control en circulo de credito
    
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
    __version = 5
    
    def __init__(self, ClaveOtorgante : int, NombreOtorgante : int, FechaCorte : int, lista_data_acreditantes : list[dict]) -> None:
        """
            params : 
                - ClaveOtorgante (str) : 
                - NombreOtorgante (str) :
                - FechaCorte (str) :
        """
        self.data_encabezado = {
            "ClaveOtorgante" : ClaveOtorgante,
            "NombreOtorgante" : NombreOtorgante,
            "FechaCorte" : FechaCorte,
            "Version" : self.__version
        }

        self.lista_data_acreditantes = lista_data_acreditantes
        self.tag_root_xml = """<?xml version="1.0" encoding="ISO-8859-1"?> """
        
        
    def element_validation(self, list_validation : list, elemnt_data : dict, name_tag : str):
        for validation in list_validation:
            if validation not in elemnt_data and elemnt_data[validation] == None:
                raise KeyError("Verifica los campos obligatorios que introdujiste")
        
        return self.Create_element(elemnt_data, name_tag)
    
    
    def __data_tag_personas(self):
        """
        descripcion : Metodo que nos permite obtener la etiqueta Personas con la data de cada uno de los acreditantes que esten dentro de la propiedad lista_data_acreditantes
        """
        data = []
        for acreditante in self.lista_data_acreditantes:
            super().__init__(acreditante)
            tag_persona = self.Persona()
            data.append(tag_persona)
        
        tag_personas = reduce(lambda tag, dat, : tag + dat, data)
        print(tag_personas)
        return f"""
    <Personas>
        {tag_personas}
    </Personas>
    """
    
    
    def get_doc(self):
        """
         descripcion : fucion que nos proporciona el archivo root con lod datos de cada uno de los acreditantes
         
         params :
            - None
            
        return (file) : archivo xml 

        """
        ClaveOtorgante = self.data_encabezado["ClaveOtorgante"]
        NombreOtorgante = self.data_encabezado["NombreOtorgante"]
        FechaCorte = self.data_encabezado["FechaCorte"]
        
        file_data = f"{ClaveOtorgante}_{NombreOtorgante}_{FechaCorte}.xml"
        tag_personas = self.__data_tag_personas()
        tag_encabezado = self.Encabezado()
        
        with open(file_data, 'w') as f:
            
            f.write(f"""
{self.tag_root_xml}
<Carga xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="/Carga.xsd">
{tag_encabezado}
{tag_personas}
</Carga>  """)
            
    
        
    def Encabezado(self):
        """
            descripcion : Metodo que nos permite retorna la eiqueta Encabezado junto a sus variables minimas.
            - ! : identificador de datos obligatorios 
            
            
            params :
                - element_data (dict) : dict que debe de contener una serie de claves minimos 
                    - ! Clave de usuario (int) | (str) : es la clave del otorgante
                    - ! Nombre de usuario (str) : razon social
                    - Identificador de medio (any): Se utiliza cuando el Usuario desea identificar de manera interna la base que envía. (identifica la db interna)
                    - ! Fecha de corte ( AAAAMMDD ) : la fecha de cuando se extra la info de la db
                    - Nota otorgnate (str) : Observiaciones sobre la informacion enviada
                    
            return : None
        """
        Name_tag = "Encabezado"
        tag_encabezado = self.Create_element(self.data_encabezado, Name_tag)
        return tag_encabezado
        
        
        


        

        
if __name__ == "__main__":
    Data_encabezado = {
        "ClaveOtorgante" : "0000080008",
        "NombreOtorgante" : "PROMOTORA PROFILE",
        "IdentificadorDeMedio" : "AZ",
        "FechaExtraccion" : 20210630,
        "NotaOtorgante" : "",
        
    }
    
    Nombre = {
        "RFC" : "CELA750508122",
        "PRIMER NOMBRE" : "ARACELI",
        "SEGUNDO NOMBRE" : "",
        "APELLIDO PATERNO" : "CERVANTES",
        "APELLIDO MATERNO" : "LUNA",
        "FECHA DE NACIMIENTO" : "19750508"
    }
    #'RFC', 'PRIMER NOMBRE', 'SEGUNDO NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'FECHA DE NACIMIENTO'
    XML = circulo_credito(
        Data_encabezado["ClaveOtorgante"],
        Data_encabezado["NotaOtorgante"], 
        Data_encabezado["FechaExtraccion"],
        [acreditante_1]
        )
    XML.get_doc()
    acreditante = Persona(acreditante_1)
    # print(acreditante.Persona())
    
    