from functools import reduce
conceptos = [{'Clave de producto o servicio.': '78181500', 'Concepto': 'SANITIZACION', 'Importe': '210.00', 'Sub total': 210.0}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'LIMPIEZA ULTRASONICA', 'Importe': '315.00', 'Sub total': 315.0}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'SERVICIO DE 30,000 KM O 2 AÑOS', 'Importe': '1527.50', 'Sub total': 1527.5}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'FILTROS DE POLVO Y POLEN DESMMONTADO', 'Importe': 
'352.50', 'Sub total': 352.5}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'LIQUIDO DE FRENOS', 'Importe': '587.50', 'Sub total': 587.5}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'VEH-CULO DEL. TRAS. MEDIDO', 'Importe': '498.76', 'Sub total': 498.76}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'CA-DA RUEDAS DEL. AJUSTADO', 'Importe': '277.10', 'Sub total': 277.1}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'CONVERGENCIA RUEDAS DEL. AJUSTADO', 'Importe': '110.84', 'Sub total': 110.84}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'CA-DA RUEDAS TRAS. AJUSTADO', 'Importe': '110.84', 'Sub total': 110.84}, {'Clave de producto o servicio.': '78181500', 
'Concepto': 'CONVERGENCIA RUEDAS TRAS. AJUSTADO', 'Importe': '110.84', 'Sub total': 110.84}, {'Clave de producto o servicio.': '78181500', 'Concepto': 'RUEDAS EQUILIBRADO', 'Importe': '443.34', 'Sub total': 443.34}, {'Clave de producto o servicio.': '25191700', 'Concepto': 'A - TORNILLO DE PURGA DE ACEITE CON RETEN', 'Importe': '57.20', 'Sub total': 57.2}, {'Clave de producto o servicio.': '25191700', 'Concepto': 'A - ELEMENTO FILTRANTE CON JUNTA', 'Importe': '300.68', 'Sub total': 300.68}, {'Clave de producto o servicio.': '25191700', 'Concepto': 'A - FILTRO DE OLORES Y ALRGENOS', 'Importe': '1293.04', 'Sub total': 1293.04}, {'Clave de producto o servicio.': '25191700', 'Concepto': 'A - LIQUIDO FRENOS', 'Importe': '310.92', 'Sub total': 310.92}, {'Clave de producto o servicio.': '25191700', 'Concepto': 'A - ACEITE PARA MOTOR 5W40 50200 50500', 'Importe': '948.71', 'Sub total': 948.71}, {'Clave de producto o servicio.': '78181600', 'Concepto': 'MATERIAL DIVERSO', 'Importe': '454.42', 'Sub total': 454.42}, {'Clave de producto o servicio.': '78181600', 'Concepto': 'NITROGENO', 'Importe': '423.00', 'Sub total': 423.0}]


def reduce_list_dict(dict_list):
    # Función para acumular los valores de cada clave
    def accumulator(acc, item):
        for key, value in item.items():
            value = str(value)
            if key in acc:
                acc[key].append(value)
            else:
                acc[key] = [value]
        return acc
    
    # Usamos reduce para acumular los valores de cada clave en un solo objeto
    reduced_dict = reduce(accumulator, dict_list, {})
    
    return reduced_dict

def reduce_dict(dict):
    for key, value in dict.items():
        dict[key] = "\n".join(value)
    return dict
    


result = reduce_dict(reduce_list_dict(conceptos))
for key, value in result.items():
    print(value)

