"""
En este script lo que queremos es obtener una serie de valores 
- fecha de factura : 
- Num clave del producto 
- folio fiscal (este esta en el titulo de documento)
- nombre del emisor
- concepto
- subtotal
- impuestos
    - IVA
    - Ret IVA 
    - Ret ISR 
- Total
"""

import xml.etree.cElementTree as ET

tree = ET.parse("data.xml") 
root = tree.getroot()

tree_CFDI = ET.parse("./CFDI/A219EF14-71D3-11ED-8D49-9D4DF4D3414C.xml")
root_CFDI = tree_CFDI.getroot()

class reed_xml :
    def __init__(self, document) -> None:
        pass


if __name__ == "__main__":
    print(root_CFDI.tag)
    # for child in root_CFDI:
    #     print(child.tag, child.attrib)
    for child in root: 
        print(child)