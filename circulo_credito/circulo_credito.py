from functools import reduce

class circulo_credito():
    """
    Clase que nos proporciona una estructura definida de los parametros minimos requeridos para el control en circulo de credito
    
     El archivo debe de contener una nomenclatura especifica para que este pueda ser reconocido de la manera adecuada :
     
datos a obtener
 - Clave de usuario
 - Nombre de usuario
 - Fecha de corte ( AAAAMMDD )
 - extencion xml

La información dentro del archivo se divide en 4 secciones
I. cliente
- RFC
- Primer nombre
- Segundo y otros nombres
- Apellido Paterno
- Segundo Apellido
- Fecha de Nacimiento
 
II. Domicilio
- Calle
- Número Exterior
- Número Interior
- Colonia
- Delegación o Municipio
- Ciudad
- Estado
- Código Postal


III.Empleo o Actividad Económica:
- Nombre o Razón Social del Empleador


IV. Crédito :
- Clave del Usuario que reporta el crédito
- Nombre del Usuario que reporta el crédito
- Número Crédito Vigente
- Tipo de Responsabilidad
- Tipo de Crédito
- Tipo de Producto
- Moneda
- Frecuencia de Pago
- Monto de Pago
- Fecha de Apertura
- Fecha del Último Pago
- Fecha de Apertura
- Fecha del Último Pago
- Monto del Crédito a la Originación
- Plazo en Meses
- Fecha de la Última Disposición o Compra
- Fecha del reporte, Actualización o Corte
- Crédito Máximo Utilizado
- Saldo Actual
- Saldo Vencido
- Forma de Pago o Pago Actual
- Fecha del Primer Incumplimiento
- Saldo Insoluto del Principal
- Monto del Último Pago
    
    """
    def __init__(self, ClaveOtorgante : int, NombreOtorgante : int, FechaCorte : int) -> None:
        """
            
            params : 
                - ClaveOtorgante (str) : 
                - NombreOtorgante (str) :
                - FechaCorte (str) :
        """
        
        self.ClaveOtorgante =  ClaveOtorgante
        self.NombreOtorgante = NombreOtorgante
        self.FechaCorte = FechaCorte
        self.tag_root_xml = """<?xml version="1.0" encoding="ISO-8859-1"?> """
        
        
               
    def get_doc(self):
        
        """
    descripcion : fucion que nos proporciona un archivo con el root del xml

        """
        file_data = f"{self.ClaveOtorgante}_{self.NombreOtorgante}_{self.FechaCorte}.xml"    
        with open(file_data, 'w') as f:
            f.write(f"""
{self.tag_root_xml}
<Carga xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="/Carga.xsd">
{self.encabezado}

</Carga> 
                   
                    """)
            
    
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
        
    def element_validation(self, list_validation : list, elemnt_data : dict, name_tag : str):
        for validation in list_validation:
            if validation not in elemnt_data and elemnt_data[validation] == None:
                raise KeyError("Verifica los campos obligatorios que introdujiste")
        
        return self.Create_element(elemnt_data, name_tag)
    
    
    def Encabezado(self, element_data : dict):
        """
            Clave de usuario
            Nombre de usuario
            Fecha de corte ( AAAAMMDD )
            extencion xml
        """
        
        list_validation = ['ClaveOtorgante', 'NombreOtorgante', 'IdentificadorDeMedio', 'FechaExtraccion', 'NotaOtorgante', 'Version']
        
        Name_tag = "Encabezado"
        
        self.encabezado = self.element_validation(list_validation, element_data, Name_tag)
        
        

    


    
class Persona():
    def __init__(self):
        pass
    
    
    def Persona(self):
        self.Tag_Nombre = self.Nombre()
        self.Tag_Domicilio = self.Domicilios()
        self.Tag_Empleos = self.Empleos()
        self.Tag_Cuenta = self.Cuenta() 
    
    
    def Nombre(self, element_data : dict): 
        list_validacion = ['RFC', 'PRIMER NOMBRE', 'SEGUNDO NOMBRE', 'APELLIDO PATERNO', 'APELLIDO MATERNO', 'FECHA DE NACIMIENTO' ]
        Name_tag = "Persona" 
        self.element_validation(list_validacion, element_data,)
        return f"""
        <Personas>
        
        </Personas>
        """

    def Domicilios(self):
        pass
    
    
    def Empleos(self):
        pass
    
    
    def Cuenta(self):
        pass 
        
    
if __name__ == "__main__":
    Data_encabezado = {
        "ClaveOtorgante" : "0000080008",
        "NombreOtorgante" : "PROMOTORA PROFILE",
        "IdentificadorDeMedio" : "AZ",
        "FechaExtraccion" : 20210630,
        "NotaOtorgante" : "",
        "Version": 5
    }
    client_0 = circulo_credito(
        Data_encabezado["ClaveOtorgante"],
        Data_encabezado["NotaOtorgante"], 
        Data_encabezado["FechaExtraccion"]
        )
    print(Data_encabezado.keys())
    client_0.Encabezado(Data_encabezado)
    client_0.get_doc()