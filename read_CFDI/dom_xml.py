from xml.dom.minidom import parse, parseString

path = "./CFDI/A219EF14-71D3-11ED-8D49-9D4DF4D3414C.xml"

document = parse(path)


with open(path) as f:
    document = parse(f)



document_2 = parseString("""\
<?xml version="1.0" encoding="UTF-8"?>
<cfdi:Comprobante xmlns:cfdi="http://www.sat.gob.mx/cfd/3" xmlns:bfa="urn:com.sap.b1i.bizprocessor:bizatoms" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv33.xsd" Version="3.3" Serie="FE" Folio="8150" Fecha="2022-12-01T17:55:29" Sello="G+P93mitj7mkYwfI/Pstvt0AI+WtPiorNCrT55cFmPmohWHNkD7QRmxBiiQFWFEKobXfGr1J1N7Ejw+8A02gsMDv4mJq4O3qE0d2VTSeIaApf3WDcOM64MU7DBs99hgMac+jsPD9y4Fufw+Y5h3P5g0FVX5bDSg2XnYvGGaK1APk0hUJ6p2qyPoB1ommeMTc2lmsNI3kvpD3d+SgoKiKmCA6KypTM7AAevBbw4VMXQqUcf2eHiEkmkoFJDsaRAuMcnTptvFVKULG66VnwUo6/4E/0uHCzF5z3P0+ouW0uIrH6JdqVvNqdt87Pxf1CqPSy6cfiZCQ2heKInW/DOh55g==" FormaPago="99" NoCertificado="00001000000500097351" Certificado="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" SubTotal="22000.00" Moneda="MXN" Total="25520.00" TipoDeComprobante="I" MetodoPago="PPD" LugarExpedicion="06470">
                    <cfdi:Emisor Rfc="EDR831004D61" Nombre="ESPAMEX DISTRIBUCIONES Y REPRESENTACIONES, S.A DE C.V." RegimenFiscal="601" />
                    <cfdi:Receptor Rfc="PPR0610168Z1" Nombre="PROMOTORA PROFILE S.A.P.I. DE C.V. SOFOM. ENR." UsoCFDI="G03" />
                    <cfdi:Conceptos>
                      <cfdi:Concepto ClaveProdServ="22101900" Cantidad="1.000000" ClaveUnidad="E48" Descripcion="SUMINISTRO" ValorUnitario="22000.000000" Importe="22000.000000">
                        <cfdi:Impuestos>
                          <cfdi:Traslados>
                            <cfdi:Traslado Base="22000.000000" Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="3520.000000" />
                          </cfdi:Traslados>
                        </cfdi:Impuestos>
                      </cfdi:Concepto>
                    </cfdi:Conceptos>
                    <cfdi:Impuestos TotalImpuestosTrasladados="3520.00">
                      <cfdi:Traslados>
                        <cfdi:Traslado Impuesto="002" TipoFactor="Tasa" TasaOCuota="0.160000" Importe="3520.00" />
                      </cfdi:Traslados>
                    </cfdi:Impuestos>
                  <cfdi:Complemento><tfd:TimbreFiscalDigital xmlns:tfd="http://www.sat.gob.mx/TimbreFiscalDigital" xsi:schemaLocation="http://www.sat.gob.mx/TimbreFiscalDigital http://www.sat.gob.mx/sitio_internet/cfd/TimbreFiscalDigital/TimbreFiscalDigitalv11.xsd" Version="1.1" UUID="A219EF14-71D3-11ED-8D49-9D4DF4D3414C" FechaTimbrado="2022-12-01T17:55:46" SelloCFD="G+P93mitj7mkYwfI/Pstvt0AI+WtPiorNCrT55cFmPmohWHNkD7QRmxBiiQFWFEKobXfGr1J1N7Ejw+8A02gsMDv4mJq4O3qE0d2VTSeIaApf3WDcOM64MU7DBs99hgMac+jsPD9y4Fufw+Y5h3P5g0FVX5bDSg2XnYvGGaK1APk0hUJ6p2qyPoB1ommeMTc2lmsNI3kvpD3d+SgoKiKmCA6KypTM7AAevBbw4VMXQqUcf2eHiEkmkoFJDsaRAuMcnTptvFVKULG66VnwUo6/4E/0uHCzF5z3P0+ouW0uIrH6JdqVvNqdt87Pxf1CqPSy6cfiZCQ2heKInW/DOh55g==" NoCertificadoSAT="00001000000505600468" SelloSAT="GHZrGG1zGq6NLVba0HbuoSDxXC/+oImHwDT5Ggb1/k+PUD3JpYTd9Vs15Rh8dEIp5UgB21QtLOiusk5ZwHXaAgcdCcrYd3tyVVVfoMgy/JNm2Bmsa69/bfq4/916+7MDNzDxC4jix6O7I2Plzw/2pEUjqWidipfsaQYZAmvRBBWnHaUPBGyKqwXGKOYZURbtt06fZYgTVHdypDapZLFKK6yIgl5NxWtoIQV/YyG0wcF22VXYqogYsneteJ/1xaYk04Zo9H0lqFdxGJBctp6bAtvn3GRMi0T2XffQvVsDT+ja6DXqF9wCwR4SmhZ/Z1aGLF06qgh2bqQBdIJueQ6qig==" RfcProvCertif="EME000602QR9" /></cfdi:Complemento></cfdi:Comprobante>
""")

if __name__ == "__main__":
    dtd = document.doctype
    print(dtd)
    # print(dtd.entities["custom_entity"].childNodes)
    print(document.documentElement)