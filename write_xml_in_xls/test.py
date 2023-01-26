import xml.etree.cElementTree as ET

# Carga el archivo XML en un árbol de elementos
fact_pago_emitida = "read_CFDI/2021/Enero/Emitidas/2f99dd73-df61-4481-bc02-34010db1fd3a.xml"

tree = ET.ElementTree(file=fact_pago_emitida)
root = tree.getroot()

# Busca el elemento "pago10:DoctoRelacionado" en el árbol
docto_relacionado = root.find(root.tag)

# Imprime el elemento encontrado
print(docto_relacionado)
print(root.attrib)