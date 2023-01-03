from hashlib import new

from reedclients import reedClient
from datetime import date, datetime  as dt
from calendar import monthrange
#TODO: metodo que nos permita obtener el email


Path = "./clients.xlsx"

class processValidator():

    def __init__(self, file_path: str, sheet_name = " ",):
        self.current_date = date.today()
        self.dias_anteriores_corte = 3
        # instancia de el doc excel 
        Excel_doc = reedClient(file_path=file_path)
        self.Excel_document = Excel_doc

        # si sheet_name no esta vacio se establece para trabajar con ella 
        if sheet_name != " ":
            self.sheet_name = Excel_doc.set_sheet_name(sheet_name)
        print(self.current_date)

    
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
        numero_dias_mes = monthrange(int(año_actual), int(mes_actual) - 1)

        #lista de los dias donde se enviaran los emails
        fechas_envios_emails = []
        for date in fechas_corte:
            print("bucle", date)
            #si el dia actual es menor que los dias que se restan para enviar el email
            if int(date) < dias_anteriores_corte :
                print("validacion")
                #entonces a la fecha del corte se le suma el numero dia dias en el mes 
                print(numero_dias_mes)
                date += numero_dias_mes[1]

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
        fechas["fechas_corte"] = fechas_corte
        return fechas


    def _get_day(self, list_dates: list):
        dias = []

        #transformamos el valor datetime para que solo nos quede el dia
        for date in list_dates:
            dateS = dt.isoformat(date.value)
            fecha = dateS.split("T")[0]
            dia = fecha.split("-")[-1]
            print (f"""
            dia {dia}
            fecha {fecha}
            """)

            dias.append(int(dia))

        return dias


    def _get_email(self):
        print("get email")
        for column in list(self.sheet_name.columns):
            for cell in column:
                if "correo" == cell.value:
                    print("validacion correos")
                    correos = column

        correos = [ item.value for item in correos if item.value != "correo"]
        return correos

        
        

    def get_fechas_corte(self):
        """
        funcion que nos permite obtener las fechas de corte de ccada cliente 
        """

        # por cada una de las columnas y cada una de las celasda si hay una celda de fecha
        #se asigna a cutoff_date como una lista 
        for column in list(self.sheet_name.columns):
            for cell in column:
                if "fecha" in cell.value:
                    self.cutoff_date = list(column)

                    # obtenemos todos los valores menos la celda con el titulo 
                    self.cutoff_date = self.cutoff_date[1:]
                break                

        #operamos las fechas para obtener las proximas a vencer
        self._get_day(self.cutoff_date)
        self._evalue_date(self.cutoff_date, self.dias_anteriores_corte)


    def get_date(self,):
        fechas = self._evalue_date(self.cutoff_date, 3)
        correo = self._get_email()
        print(f"""
        data:
        fecha envios de correos : {fechas}
        correos: {correo}
        """)
        
doc = processValidator(Path,"clients credito" )
doc.get_fechas_corte()
doc.get_date()