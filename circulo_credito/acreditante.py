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
        