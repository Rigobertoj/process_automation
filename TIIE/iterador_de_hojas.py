from edit_file_credit import TIIE_file_edit_from_py

class iterador_hojas():
    def __init__(self, path_file: str):
        self.path_file = path_file
        Excel_document = TIIE_file_edit_from_py(path_file)
        self.Excel_document = Excel_document


    def iterador_hoja(self):
        hojas = self.Excel_document.get_sheet_names()
        for sheet in hojas:
            self.Excel_document.set_sheet_name(sheet)     