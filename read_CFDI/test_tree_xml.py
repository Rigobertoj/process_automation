"""
En este script lo que queremos es obtener una serie de valores 
- fecha de factura : 
- Num clave del producto 
- folio fiscal (este esta en el titulo de documento)
- nombre del emisor
- concepto
- subtotal
- impuestos
    - IVA : root_CFDI[2][0][0][0][0].attrib["TasaOCuota"]
    - Ret IVA 
    - Ret ISR 
- Total
"""

# asi se importa la libreria de xml
import xml.etree.cElementTree as ET

CFDI_TASA_0 = "./CFDI/7513B197-3F46-4807-B4E6-1001AAA07248.xml"
CFDI_TASA_SIMPLE = "./CFDI/A219EF14-71D3-11ED-8D49-9D4DF4D3414C.xml"

#obtenemos el objeto xml

tree = ET.parse(CFDI_TASA_0)

#obtenemos el root del XML 
root = tree.getroot()

# imprimimos el 
print(f"rooot : {root.tag}")


print(root.tag)
    # for child in root_CFDI:
    #     print(child.tag, child.attrib)
# for child in root: 
#     print(child.attrib)


# me permite obtener los datos de emisor del CFDI 
print("0 ", root[0].attrib)

# me permite obtener los datos del receptor del CFDI 
print(root[1].attrib)

# me permite obtener los datos de compra del producto
print(root[2][0].attrib)

# me permite obtener los datos de los impuestos trasladados 
print(root[2][0][0][0][0].attrib["TasaOCuota"])

conceptos = root[2]
print(conceptos.attrib)

print("products")
for concepto in conceptos:
    print(f"""
    f{concepto.attrib}
    f{concepto[0][0][0].attrib}
    _____________________________________________________________
    """)