from reedclients import reedClient
from datetime import date, datetime  as dt
from calendar import monthrange
from utils.day import day

#TODO: metodo que nos permita obtener el email 

Path = "./clients/clients.xlsx"


class processValidator():
    """
    atributos:
        Excel_document ( reedclients ) : instancia del documento excel para su manipulacion 
        sheet_name ( str ) : nombre de la hoja de excel la cual queremos procesar
        current_date ( datetime ) : datetime para obtener el dia actual 
        dias_anteriores_corte ( int ) : dias a evaluar para antes del corte para el envio del email

    explicacion : 
        clase que nos permite validar cual sera el dia que se devera enviar un email evaluando x cantidad de dias antes de su corte del mes
    """


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

    
    def _evalue_date(self, list_dates: list[str], dias: int ) -> dict[list, list]:
        """
        param :
            list_dates ( list[str] ) : es una lista de fechas en strings
            dias ( int ) : dias antes de la fecha de corte

        explicacion :
            esta funion lo que nos permite es retornar la fecha de envio de un email dependiendo de los dias que se desee de enviar entes de la fecha de corte. \n 
        
        return dict[fechas_envios_emails, dias_de_corte] 
        """
        fechas = {}

        #dias anteriores a la fecha del pago del credito
        dias_anteriores_corte = dias
        
        #los dias de las fechas de corte de cada cliente 
        fechas_corte = day.get_days(list_dates=list_dates)

        #fecha actul
        año_actual, mes_actual, dia_actual = str(self.current_date).split("-")

        #dias que tiene el mes actual 
        numero_dias_mes_pasado = monthrange(int(año_actual), int(mes_actual)- 1)

        #lista de los dias donde se enviaran los emails
        fechas_envios_emails = []
        for date in fechas_corte["dias_de_corte"]:
            #si el dia actual es menor que los dias que se restan para enviar el email
            if int(date) < dias_anteriores_corte :
                #entonces a la fecha del corte se le suma el numero dia dias en el mes 
                date += numero_dias_mes_pasado[1]

                # para asi restar el limite de dias antes de enviar el email y salga que es el mes anteriorse
                dia_envio_email = date - dias_anteriores_corte 

                #se resta uno al mes ya que no estara dentro del mismo mes de la fecha de corte
                mes_anterios = int(mes_actual)
                mes_anterios -= 1

                fecha_envio_email = f"{año_actual}-{mes_anterios}-{dia_envio_email}"
                fechas_envios_emails.append(fecha_envio_email)
            else:
                dia_envio_email = date - dias_anteriores_corte
                fecha_envio_email = f"{año_actual}-{mes_actual}-{dia_envio_email}"
                fechas_envios_emails.append(fecha_envio_email)

        fechas["fechas_envios_emails"] = fechas_envios_emails
        fechas["dias_de_corte"] = fechas_corte["dias_de_corte"]
        return fechas


    def _get_day(self, list_dates: list):
        fechas_dias = {
            "fechas_de_corte": list_dates
        }
        dias = []
        #transformamos el valor datetime para que solo nos quede el dia
        for date in list_dates:
            dateS = dt.isoformat(date.value)
            fecha = dateS.split("T")[0]
            dia = fecha.split("-")[-1]

            dias.append(int(dia))

        fechas_dias["dias_de_corte"] = dias
        return fechas_dias


    def get_validation(self) -> list:
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
        fechas = self.Excel_document._get_colum("fecha")[1:]

        # obtenemos la validacion de las fechas
        fechas_envio_mail = self._evalue_date(fechas, 3)
        fechas = self.Excel_document._delete_cell("fecha", fechas) #--

        #parametrisable primer arg correo
        correos = self.Excel_document._get_colum("correo")
        correos = self.Excel_document._delete_cell("correo",correos) #--


        for correo, dia, fecha_envio_mail, fechas in zip(correos, fechas_envio_mail["dias_de_corte"],fechas_envio_mail["fechas_envios_emails"], fechas ):
            data["correos"].append(correo)
            data["fechas_envio"].append(fecha_envio_mail)
            data["fecha_corte"].append(fechas)

        print(data["fechas_envio"])
        return data["fechas_envio"]



if __name__ == "__main__":
    doc = processValidator(Path,"clients credito" )
    doc.get_validation()