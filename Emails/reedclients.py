from openpyxl import load_workbook
Path = "clients/clients.xlsx"

class reedClient():
    
    def __init__(self,file_path: str, ):
        self.path_file = file_path
        self.Excel_document = load_workbook(file_path)

    
    def get_shenames(self) -> list[str]:
        """retorna una lista con el nombre de las hojas en el documento"""
        print(self.Excel_document.sheetnames)
        return self.Excel_document.sheetnames

    def set_sheet_name(self, sheet_name: str,):
        """establece la hoja con la que se va atrabajar en el documento"""
        self.sheet_name = self.Excel_document[sheet_name]
        return self.sheet_name

    def _delete_cell(self, tittle: str, data_list: list):
        """Metodo que nos permite eliminar una cellda de la columna
        utilicece para eliminar el titulo de la columna
        """
        new_lits = [item.value for item in data_list if item.value != tittle]
        return new_lits


    def _get_colum(self, name_colum: str,) -> list:
        """ metodo que nos permite obtener cualquier columna de la hoja de excel"""
        for colum in list(self.sheet_name.columns):
            for cell in colum:
                if name_colum in str(cell.value):
                
                    column_celda = list(colum)
                    print(name_colum)
                    return column_celda

                    
    def _get_values(self, column:list) -> list:
        """retorna una lista con los valores de la columna que se le introduscan"""
        column_value = [cell.value  for cell in column]
        return column_value

    
    def save(self,):
        """
        Guarda los cambios en el documento
        este de de estar sin abrir para que los cambios se guarden correctamente
        """
        self.Excel_document.save(self.path_file)

# clients = reedClient(Path)
# clients.get_shenames()
# clients.set_sheet_name("clients credito")


