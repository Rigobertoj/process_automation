from openpyxl import load_workbook
import pandas as pd
import os

class Read_xlsx():
    
    def __init__(self, file_path : str, worksheet_name : str):
        if self._is_valid_path(file_path):
            try : 
                self.file_path = file_path   
                self.wb = load_workbook(file_path)
            
                self.set_work_sheet(worksheet_name)
                self.df = self.__get_data_frame__(file_path)
            except KeyError :
                raise KeyError(f"la worksheet : {worksheet_name},  no existe")
        else:
            raise ValueError("Introduce una ruta o nombre de archivo valido")
    
    
    def  __str__(self) -> str:
        return f"""
    wb path : {self.file_path}
    ws set  : {self.ws}
        """
                
    
    def set_work_sheet(self, sheet_name : str):
        try :
            if sheet_name in self.wb.sheetnames:
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
        
    
    def __get_data_frame__(self, path):
        return pd.read_excel(path)
    
    
    def filter_Tipe(self, type : str):
        return self.df[self.df["Tipo."] == f"{type}"]
        
        
        

def main():
    wb_path = "Enero_ingresos.xlsx"
    ws_name = "Conjunto de gastos 2"
    wb_obj = Read_xlsx(wb_path, ws_name)
    data = wb_obj.filter_data()
    print(data)

if __name__ == '__main__':
    main()