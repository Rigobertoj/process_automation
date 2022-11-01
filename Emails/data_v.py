from reedclients import reedClient
from datetime import date, datetime  as dt, timedelta

#TODO: metodo que nos permita obtener el email 

Path = "./clients/clients.xlsx"


class processValidator():
    def __init__(self, file_path: str, sheet_name: str = " ",) -> None:
        """
        params: 
            file_path ( str ) : Ruta del documento excel
            sheet_name ( str ) : opccional. Nombre de la hoja a procesar.

        explicacion :
            contructor que nos permite instanciar el documento excel junto a la hoja que queremos procesar
        """

        # instancia de el doc excel 
        Excel_doc = reedClient(file_path=file_path)
        self.Excel_document = Excel_doc
        
        #atributo del dia actual
        self.current_date = date.today()
        self.dias_anteriores_corte = 3

        # si sheet_name no esta vacio se establece para trabajar con ella 
        if sheet_name != " ":
            self.sheet_name = Excel_doc.set_sheet_name(sheet_name)

    def validacion_de_fecha(self):
        """
        explicacion: 
            pendiente a testeo 
        """
        data = {
            "correos": [],
            "fechas_envio": [],
            "fecha_corte": []
        }

        #obtenemos la columna de las fechas
        fechas = self.Excel_document.get_colum("fecha")[1:]
        correos = self.Excel_document.get_colum("correo")[1:]
        for date, correo in zip(fechas, correos):
            fecha_envio = date.value - timedelta(days=self.dias_anteriores_corte)
            data["fechas_envio"].append(fecha_envio)
            data["correos"].append(correo.value)
            data["fecha_corte"].append(date.value)

        return data




if __name__ == "__main__":
    clients = processValidator(Path, "clients credito")
    print(clients.validacion_de_fecha())