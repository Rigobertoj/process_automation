from datetime import date, datetime  as dt

class day():
    """
    pendiente a testeo
    description class:
        clase que nos permite evaluar una lista de fechas retornar algun valor que necesitemos de las mismas

    """
    def __init__(self, ) -> None:
        pass
    
    def get_days(self, list_dates: list):
        """
        

        """
        fechas_dias = {
            "fechas_de_corte": list
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

if __name__ == "__main__":
    today = day()