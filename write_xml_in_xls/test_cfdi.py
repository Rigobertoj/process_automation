from app_cfdi.Impuestos.impuestos import Impuestos
from app_cfdi.Nomina.Nomina import Nominas
from app_cfdi.Fechas.Fecha import Fechas_xml

def test_nomina():
    path_emitidas = "C:/Users/User/Documents/Rigo/2023/XML/Emitidas/Febrero/Febrero"
    Nomina = f"{path_emitidas}/0B8B6950-EAB0-4DA2-B14A-B09B6DB8846E.xml"
    nomina = Nominas(Nomina)
    print(nomina.get_importes_nominas())
    
def test_Impuestos():
    path_cfdi = "C:/Users/User/Documents/Rigo/2023/XML/Recibidas/Enero/7A6A42D0-0448-479A-B996-75A734AFBCA3.xml"
    impuesto = Impuestos(path_cfdi)
    print(impuesto.get_taxes())

def test_fecha():
    path_cfdi = "C:/Users/User/Documents/Rigo/2023/XML/Recibidas/Enero/7A6A42D0-0448-479A-B996-75A734AFBCA3.xml"
    f = Fechas_xml(path_cfdi)
    print(f.fecha_facturacion())

if __name__ == '__main__':
    RFC = "PPR0610168Z1"
    def asus_home(RFC : str):
        home_asus_xml_path = "C:/Users/rigoj/Documents/profile/contabilidad/2023/XML/Enero/Ingresos/1d1a55d4-1eaa-4890-9197-6aeda12e2f51.xml"
        # cfdi = CFDI(home_asus_xml_path, RFC)
        # data = cfdi.main()
        # for key, value in data.items():
        #     print(f"""
        #     {key} : {value}""")

        i = Impuestos(home_asus_xml_path)
        print(i.get_taxes())

    # print("Enter")
    # asus_home(RFC)
    test_nomina()
    test_Impuestos()
    test_fecha()