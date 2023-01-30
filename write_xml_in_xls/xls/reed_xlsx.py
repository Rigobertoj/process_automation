import openpyxl 
import os

class Read_xlsx(openpyxl):
    
    def __init__(self, file_path : str):
        
        if self._is_valid_path(file_path):     
            self.file_path = file_path   
            self.wb = openpyxl.load_workbook(file_path) 
        else:
            raise ValueError("Introduce una ruta o nombre de archivo valido")
    
    
    def  __str__(self) -> str:
        return f"""
    wb path : {self.file_path}
    wb set : {self.ws}
        """
                
    
    def set_work_sheet(self, sheet_name : str):
        try :
            self.ws = self.wb[sheet_name]
        except ValueError:
            pass
    
    
    def _is_valid_path(self, path : str):
        """Descripcion : metodo que nos permite validar si un string es una ruta de una archivo

        Params:
            path (str): String que se quiere validar si es una ruta de una archivo

        Returns:
            boolean: retorna True o False dependiendo de la validacion 
        """
        if os.path.isabs(path) :
            return True
        elif not os.path.isabs(path) :
            return True
        else:
            return False
        
        
if __name__ == '__main__':
    wb_path = "Enero_ingresos.xlsx"
    wb_obj = Read_xlsx(wb_path)
    print(wb_obj)