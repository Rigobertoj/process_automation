from hashlib import new

from numpy import half
from reedclients import reedClient
import openpyxl 
from datetime import date, datetime  as dt
from calendar import monthrange
#TODO: metodo que nos permita obtener el email 

Path = "./clients.xlsx"

class processValidator():

    def __init__(self, file_path: str, sheet_name = " ",):
        # instancia de el doc excel 
        Excel_doc = reedClient(file_path=file_path)
        self.Excel_document = Excel_doc
        
        self.current_date = date.today()
        self.dias_anteriores_corte = 3

        # si sheet_name no esta vacio se establece para trabajar con ella 
        if sheet_name != " ":
            self.sheet_name = Excel_doc.set_sheet_name(sheet_name)

    def _delete_cell(self, tittle: str, data_list: list):
        new_lits = [item.value for item in data_list if item.value != tittle]
        return new_lits


    def _get_colum(self, name_colum: str,) -> list:
        for colum in list(self.sheet_name.columns):
            for cell in colum:
                if name_colum in str(cell.value):
                    column_data = colum
                    return column_data

    
    def _evalue_date(self, list_dates: list[str], dias: int ) -> dict[list, list]:
        fechas = {}
        """
        list_dates : list[str] es una lista d fechas
        dias: int dia para antes de la fecha de corte

        esta funion lo que nos permite es retornar la fecha de envio de un email dependiendo de los dias que se desee de enviar entes de la fecha de corte
        """

        #dias anteriores a la fecha del pago del credito
        dias_anteriores_corte = dias
        
        #los dias de las fechas de corte de cada cliente 
        fechas_corte = self._get_day(list_dates)

        #fecha actul
        año_actual, mes_actual, dia_actual = str(self.current_date).split("-")

        #dias que tiene el mes actual 
        numero_dias_mes_pasado = monthrange(int(año_actual), int(mes_actual) - 1)

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
                mes_actual = int(mes_actual)
                mes_actual -= 1

                fecha_envio_email = f"{año_actual}-{mes_actual}-{dia_envio_email}"
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



    def get_date(self,):
        #obtenemos la culumna de fechas de corte y eliminamos la celda del titulo
        fechas = self._get_colum("fecha")[1:]
        fechas = self._evalue_date(fechas, 3)
        correo = self._get_colum("correo")
        correos = self._delete_cell("correo",correo)
        print(f"""
        data:
        fecha envios de correos : {fechas}
        correos: {correos}
        """)
        
doc = processValidator(Path,"clients credito" )
doc.get_date()