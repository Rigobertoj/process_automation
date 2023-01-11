from functools import reduce
from acreditante import Persona
acreditante_1 = {'RFC': 'RARC860607497', 'PRIMER NOMBRE': 'CARLOS', 'SEGUNDO NOMBRE': 'MANUEL', 'APELLIDO PATERNO': 'RAMIREZ', 'APELLIDO MATERNO': 'ROSALES', 'FECHA DE NACIMIENTO': 20141127, 'CALLE': 'SANTA TERESA DE JESUS', 'NUMERO EXTERIOR': 266, 'NUMERO INTERIOR': None, 'COLONIA': 'CAMINO REAL', 'DELEGACION O MUNICIPIO': 'ZAPOPAN', 'CIUDAD': 'ZAPOPAN', 'ESTADO': 'JALISCO', 'CODIGO POSTAL': 45040, 'NOMBRE O RAZON SOCIAL': 'CARLOS MANUEL RAMIREZ ROSALES', 'DIRECCION': 'SANTA TERESA DE JESUS 266', 'COLONIA POBLACIONAL': 'CAMINO REAL', 'DELEGACION MUNICIPAL': 'ZAPOPAN', 'CIUDAD E': 'ZAPOPAN', 'ESTADO E': 'JALISCO', 'CP E': 45040, 'CLAVE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NOMBRE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NUMERO CREDITO VIGENTE': None, 'TIPO DE RESPONSABILIDAD': 'I', 'TIPO DE CREDITO ': 'P', 'TIPO DE PRODUCTO': 'AR', 'MONEDA': 'MX', 'FRECUENCIA DE PAGO': 'M', 'MONTO DE PAGO': 80000, 'FECHA DE APERTURA': 20211206, 'FECHA DE ULTIMO PAGO': 20220825, 'MONTO DEL CREDITO A LA ORIGINACION': 2000000, 'PLAZO EN MESES': 24, 'FECHA DE LA ULTIMA DISPOSICION O COMPRA': 20211206, 'FECHA DEL REPORTE ACTUALIZACION O CORTE': 20230113, 'CREDITO MAXIMO UTILIZADO': 2000000, 'SALDO ACTUAL': 2000000, 'SALDO VENCIDO ': 583878.5893709798, 'FORMA DE PAGO O PAGO ACTUAL': 7, 'FECHA DEL PRIMER INCUMPLIMIENTO': 20220306, 'SALDO INSOLUTO DEL PRINCIPAL': 2000000, 'MONTO DEL ULTIMO PAGO': 28501.87}

    
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
    
    