from app_cfdi.Impuestos.impuestos import Impuestos
from app_cfdi.Nomina.Nomina import Nominas


def test_nomina():
    path_emitidas = "C:/Users/User/Documents/Rigo/2023/XML/Emitidas/Febrero/Febrero"
    Nomina = f"{path_emitidas}/0B8B6950-EAB0-4DA2-B14A-B09B6DB8846E.xml"
    nomina = Nominas(Nomina)
    print(nomina.get_importes_nominas())

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