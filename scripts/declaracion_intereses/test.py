conjunto_acreditados = {
"PUBLICO EN GRAL",
"EN CONCRETO 1006",
"PRO-VIVAZ MEXICANA",
"COLON 590 ",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"RAMON ARTURO VAZQUEZ RAYAS",
"RAFAEL GONZALEZ FRANCO DE LA PEZA",
"PRO-VIVAZ MEXICANA",
"RAFAEL GONZALEZ FRANCO DE LA PEZA",
"RAFAEL GONZALEZ FRANCO DE LA PEZA",
"ALAN YASIR SALAS CARLOS",
"PRO-VIVAZ MEXICANA",
"JOSE RICARDO JUAREZ DIAZ",
"INNOVACION INMOBILIARIA DALOSA",
"INNOVACION INMOBILIARIA DALOSA",
"INNOVACION INMOBILIARIA DALOSA",
"PRO-VIVAZ MEXICANA",
"CARLOS GONZALEZ REYES",
"PRO-VIVAZ MEXICANA",
"TEPETATE PROP",
"TEPETATE PROP",
"JOSE LUIS SALAS GUERRERO",
"INNOVACION INMOBILIARIA DALOSA",
"INNOVACION INMOBILIARIA DALOSA",
"PRO-VIVAZ MEXICANA",
"TEPETATE PROP",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"ALMA ELIZABETH VEGA BARAY",
"ALMA ELIZABETH VEGA BARAY",
"INNOVACION INMOBILIARIA DALOSA",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"INTRADESARROLLOS",
"TEPETATE PROP",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"SERVICIOS JURIDICOS INTEGRALES DALOSA",
"EXCLUSIVAS MARBO",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"ALMA ELIZABETH VEGA BARAY",
"INNOVACION INMOBILIARIA DALOSA",
"PRO-VIVAZ MEXICANA",
"INNOVACION INMOBILIARIA DALOSA",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"ENDUZ",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"PRO-VIVAZ MEXICANA",
"CAVSA COLIMA AUTOMOTRIZ",
"DESARROLLOS PATRIA HIPODROMO",
}

clientes = {
"ALAN YASIR SALAS CARLOS",
"ALMA ELIZABETH VEGA BARAY",
"CARLOS GONZALEZ REYES",
"CAVSA COLIMA AUTOMOTRIZ",
"COLON 590 ",
"DESARROLLOS PATRIA HIPODROMO",
"EN CONCRETO 1006",
"ENDUZ",
"EXCLUSIVAS MARBO",
"INNOVACION INMOBILIARIA DALOSA",
"INTRADESARROLLOS",
"JOSE LUIS SALAS GUERRERO",
"JOSE RICARDO JUAREZ DIAZ",
"PRO-VIVAZ MEXICANA",
"PUBLICO EN GRAL",
"RAFAEL GONZALEZ FRANCO DE LA PEZA",
"RAMON ARTURO VAZQUEZ RAYAS",
"SERVICIOS JURIDICOS INTEGRALES DALOSA",
"TEPETATE PROP",
}

Asociados_contabilidad  = {
"ALAN YASIR SALAS CARLOS",
"DESARROLLOS PATRIA HIPODROMO",
"EN CONCRETO 1006",
"ENDUZ",
"EXCLUSIVAS MARBO",
"INNOVACION INMOBILIARIA DALOSA",
"INTRADESARROLLOS",
"JOSE LUIS SALAS GUERRERO",
"UNION DE CREDITO DE LA PROVINCIA MEXICANA, SA DE CV",
}

conjunto_cuentas_contables = {
    "Gastos por servicios financieros."

}


with open ("Acreditados Marzo 2023.txt", "w", encoding="UTF-8") as f:
    f.write("CONJUNTO CLIENTES\n\n")

    for acreditado  in conjunto_acreditados:
        f.write(f"{acreditado}\n")
    f.write(" \n")
    f.write("CLIENTES NO ASOCIADOS A CUENTAS\n\n")

    clientes_no_asociados = clientes - Asociados_contabilidad

    for acreditado in clientes_no_asociados:
        f.write(f"{acreditado}\n")

conjunto_cuentas_contables = {
    "Gastos por servicios financieros." :{ 
        "5202 01 00 00 0000" : "POR SERVICIOS",
        "1401 04 01 00 0001" : "IVA ACREDITABLE", 
        "1102 00 00 00 0000" : "BANCOS",
    },
    "Gastos por telefonia e internet." : {
        "6491 15 00 00 0000" : "Telefonia e Internet", 
        "1401 04 01 00 0001" : "IVA ACREDITABLE",
        "1102 00 00 00 0000" : "BANCOS", 
    },
    
    "Gastos software de terceros." : {
        "6403 21 00 00 0000" : "Renta de Software",
        "1401 04 01 00 0001" : "IVA Acreditable", 
        "1102 00 00 00 0000" : "Bancos Nacionales",
    }, 

    "Honorarios personas fisicas cierre de mes.": {
        "6402 10 00 00 0000" : "HONORARIOS PERSONAS FISICAS",
        "1401 04 01 00 0002" : "IVA Pendiente de Acreditar",
        "2401 08 00 00 0001" : "Retención ISR de 10%",
        "2401 07 00 00 0004" : "Retención de IVA de 10.6667%",
        "2401 12 02 00 0000" : "Honorarios y rentas"
    },

    "Honorarios personas fisicas al momento de pago." : {
        "2401 12 02 00 0000" : "Honorarios y rentas",
        "1401 04 01 00 0001" : "IVA ACREDITABLE", 
        "1401 04 01 00 0002" : "IVA Pendiente de Acreditar", 
        "1102 00 00 00 0000" : "Bancos Nacionales"
    },

    "Honorarios persona moral cierre de mes." : {
        "6402 20 00 00 0000" : "HONORARIOS PERSONAS MORALES",
        "1401 04 01 00 0002" : "IVA Pendiente de Acreditar",
        "2401 12 02 00 0000" : "Honorarios y rentas"
    },

    "Honorarios persona moral al momento de pago" : {
        "2401 12 02 00 0000" : "Honorarios y rentas",
        "1401 04 01 00 0001" : "IVA ACREDITABLE",
        "1401 04 01 00 0002" : "IVA Pendiente de Acreditar",
        "1102 00 00 00 0000" : "Bancos Nacionales",
    },

    "Impuestos diversos." : {
        "6406 00 00 00 0000" : "IMPUESTOS Y DERECHOS DIVERSOS " ,
        "1102 00 00 00 0000" : "Bancos Nacionales",
    },


    "Otros gastos." : {
        "6491 18 00 00 0000" :"Limpieza" ,
        "6491 24 00 00 0000" : "Mensajería y correos" ,
        "6491 01 00 00 0000" : "Combustibles y lubricantes",
        "6491 21 00 00 0000" : "Cuotas y Suscripciones",
        "6491 25 00 00 0000" : "IEPS",
        "1401 04 01 00 0001" : "IVA Acreditable",
        "1102 00 00 00 0000" : "Bancos Nacionales",
        },

    "Papeleria y utiles." : {
        "6491 12 00 00 0000" : "Papelería y artículos de oficina" ,
        "1401 04 01 00 0001" : "IVA Acreditable",
        "1102 00 00 00 0000" : "Bancos Nacionales",
        },

    "Servicios de mantenimiento" : {
        "6491 09 00 00 0000" : "Mantenimiento oficina",
        "1401 04 01 00 0001" : "IVA Acreditable",
        "1102 00 00 00 0000" : "Bancos Nacionales",
        }
}
# asientos_provisiones_egresos = [
#     "CASO 1",
#     "PROVISIÓN MENSUAL",
#     "6403 21 00 00 0000",
#     "1401 04 01 00 0002",
#     "2401 12 90 00 0000",

#     "2401 12 90 00 0000",
#     "1401 04 01 00 0001",
#     "1401 04 01 00 0002",
#     "1102 00 00 00 0000",

#     "CASO 2",
#     "PAGO ANUAL ANTICIPADO",

#     "1903 02 07 00 0000",
#     "1401 04 01 00 0001",
#     "1102 00 00 00 0000",

#     "6403 21 00 00 0000",
#     "1903 02 07 00 0000",
# ]