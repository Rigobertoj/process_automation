from datetime import date, datetime  as dt
from ..reedclients import reedClient
class day():
    """
    TODO:pendiente a testeo
    description class:
        clase que nos permite evaluar una lista de fechas retornar algun valor que necesitemos de las mismas

    """
    def __init__(self ) -> None:
        pass
    
    def get_days(self, list_dates):
        """
        

        """
        print(F" class day -> lista de fechas {list_dates}")
        fechas_dias = {
            "fechas_de_corte": list
        }
        dias = []
        #transformamos el valor datetime para que solo nos quede el dia
        for date in list_dates:
            print(date)
            #?para que itera
            dateS = dt.isoformat(date.value)
            print(dateS)
            fecha = dateS.split("T")[0]
            print(fecha)
            dia = fecha.split("-")[-1]
            print(dia)

            dias.append(int(dia))

        fechas_dias["dias_de_corte"] = dias
        return fechas_dias

if __name__ == "__main__":
    work_doc = reedClient("../clients/clients.xlsx")
    work_doc.get_shenames()
    today = day()