#importando un modulo y asignandole el nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese  modulo importamos 2 funciones y les cambiamos el nombre
from modulo_saludar import saludar, saludar_raro as saludar_normal
import modulo_saludar as m_saludar

#creamos las variables con los saldos
saludo = saludar("Jhostin")
saludar_raro = saludar_normal("Puto")

#mostramos los resultados
print(saludo)
print(saludar_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)
#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)