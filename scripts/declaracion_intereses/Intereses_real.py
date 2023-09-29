from read_xml import Reed_xml
import os
import pandas as pd

path_dir_xml = "C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/Resumen Intereses 2022 Familia Beruben/XML Familia Beruebn"


ACREDITANTES ={
    "ALVARO BERUBEN GALVAN":"ALVARO BERUBEN GALVAN",
    "ALVARO BERUBEN JAIME":"ALVARO BERUBEN JAIME",
    "REBECA GALVAN BLANCO":"REBECA GALVAN BLANCO",
    "REBECA LI BERUBEN GALVAN":"REBECA LI BERUBEN GALVAN"
}

def get_file_names(dir : str):
    return os.listdir(dir)

class retenciones_intereses(Reed_xml):
    def __init__(self, path_document: str) -> None:
        super().__init__(path_document)

    def get_uuid_from_xml(self,):
        childs = self.get_childs(self.root)
        element_complemento = childs.get("Complemento")
        timbre_fiscal  = self.get_childs(element_complemento).get("TimbreFiscalDigital")
        return self.get_items(timbre_fiscal).get("UUID")

    def extract_mont_real_from_intereses(self, atrb):
        childs = self.get_childs(self.root)

        path_retenciones = childs.get("Complemento")

        values = self.get_childs(path_retenciones).get('Intereses')
        return self.get_items(values).get(f'{atrb}')


def get_intereses_reales(path):
    list_names_files = get_file_names(path)
    data_intereses_reales = map(lambda name_file :retenciones_intereses(f"{path}{name_file}").extract_mont_real_from_intereses("MontIntReal"), list_names_files)
    data_perdida_por_intereses = map(lambda name_file :retenciones_intereses(f"{path}{name_file}").extract_mont_real_from_intereses("Perdida"), list_names_files)
    xml_folios = map(lambda name_file :retenciones_intereses(f"{path}{name_file}").get_uuid_from_xml(), list_names_files)
    return data_intereses_reales, data_perdida_por_intereses, xml_folios



if __name__ == "__main__":
    # Alvaro Beruben Jaime, Alvaro Beruben Galvan, Rebeca Galvan Blanco, Rebeca Li Beruben
    name_shet = "Rebeca Li Beruben"

    df = pd.read_excel("C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/Resumen Intereses 2022 Familia Beruben/Retenciones Familia Beruben.xlsx", sheet_name=name_shet)
    df["UUID"] = df["UUID"].apply(lambda UUID : str(UUID).upper())

    data_intereses_reales, data_perdida_por_intereses, xml_folios = get_intereses_reales(f"{path_dir_xml}//REBECA LI BERUBEN GALVAN/")
    
    series_interes_real = pd.DataFrame({"Intereses reales" : data_intereses_reales, "Perdida intereses" : data_perdida_por_intereses, "UUID" :xml_folios })
    series_interes_real["UUID"] = series_interes_real["UUID"].astype(str)

    df_interes_real_merge = pd.merge(df,series_interes_real, left_on="UUID", right_on="UUID")

    df_interes_real_merge.to_excel("C:/Users/Luis Carlos Gomez/Rigoberto/OneDrive - CORREDURIA 38 S.C/Contabilidad Promotora Profile/2022 Actualizado/Resumen Intereses 2022 Familia Beruben/REBECA LI BERUBEN GALVAN.xlsx")
