from edit_file_credit import TIIE_file_edit_from_py

class iterador_hojas():
    def __init__(self, path_file: str):
        self.path_file = path_file
        Excel_document = TIIE_file_edit_from_py(path_file)
        self.Excel_document = Excel_document


    def iterador_hoja(self):
        hojas = self.Excel_document.get_sheet_names()
        empty_cells = {}
        list_personas = []
        for sheet in hojas:
            self.Excel_document.set_sheet_name(sheet)
            # print(list(self.Excel_document.sheet_names.rows))
            cell_empty = self.Excel_document.get_next_cell_empty("TIIE")
            print(sheet)

            print(cell_empty)
            if cell_empty == None:
                continue

            print(f"value cell_empty {cell_empty}")
            list_personas.append(sheet)

        print(len(self.Excel_document.get_sheet_names()))
        print(len(list_personas))
        # return empty_cells

if __name__ == "__main__":
    path = 'Control de crédito mensual .xlsx'
    doc = iterador_hojas(path)
    doc.iterador_hoja()
