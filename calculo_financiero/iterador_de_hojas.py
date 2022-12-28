from edit_file_credit import TIIE_file_edit_from_py

class iterador_hojas():
    def __init__(self, path_file: str):
        self.path_file = path_file
        Excel_document = TIIE_file_edit_from_py(path_file)
        self.Excel_document = Excel_document


    def iterador_hoja(self):
        hojas = self.Excel_document.get_sheet_names()
        empty_cells = {}
        for sheet in hojas:
            self.Excel_document.set_sheet_name(sheet)
            cell_empty = self.Excel_document.get_next_cell_empty("TTIE")
            empty_cells[sheet] = cell_empty

        return empty_cells

if __name__ == "__main__":
    doc = iterador_hojas()
