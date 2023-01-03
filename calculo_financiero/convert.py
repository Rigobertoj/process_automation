class conver_value():
    def __init__(self,objeto_a_convertir: any = None):
        """
        params:
            objeto_a_convertir (any) : valores que se pretenden convertir en otro dato

        metod:
            que nos permite convertir un elemento o un objeto a un otro tipo de dato
        """

        #si el objeto_a_convertir tiene un elemento este se guarda en un atributo
        if objeto_a_convertir is not None:
            self.value = objeto_a_convertir

    def conver_string(self, objeto_a_convertir: any = None) -> str:
        """
        description:
            metod that allows to convert any object to strings
        """

        #si el paramtro tiene un elemento este re retorna en un string
        if objeto_a_convertir is not None:
            return f"{objeto_a_convertir}"

        #si el paramtro es none este retorna el string del valor en self.value
        return f"{self.value}"
        


if __name__== "__main__": 
    tranform = conver_value(12)
    value = tranform.conver_string()
    print(type(value))