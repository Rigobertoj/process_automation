data_domicilio = [
    "Número Exterior",
    "Número Interior",
    "Colonia",
    "Delegación o Municipio",
    "Ciudad",
    "Estado",
    "Código Postal",]

data_mayusculas = list(map(lambda x: x.upper(), data_domicilio))
print(data_mayusculas)

acreditante_1 = {'RFC': 'RARC860607497', 'PRIMER NOMBRE': 'CARLOS', 'SEGUNDO NOMBRE': 'MANUEL', 'APELLIDO PATERNO': 'RAMIREZ', 'APELLIDO MATERNO': 'ROSALES', 'FECHA DE NACIMIENTO': 20141127, 'CALLE': 'SANTA TERESA DE JESUS', 'NUMERO EXTERIOR': 266, 'NUMERO INTERIOR': None, 'COLONIA': 'CAMINO REAL', 'DELEGACION O MUNICIPIO': 'ZAPOPAN', 'CIUDAD': 'ZAPOPAN', 'ESTADO': 'JALISCO', 'CODIGO POSTAL': 45040, 'NOMBRE O RAZON SOCIAL': 'CARLOS MANUEL RAMIREZ ROSALES', 'DIRECCION': 'SANTA TERESA DE JESUS 266', 'COLONIA POBLACIONAL': 'CAMINO REAL', 'DELEGACION MUNICIPAL': 'ZAPOPAN', 'CIUDAD E': 'ZAPOPAN', 'ESTADO E': 'JALISCO', 'CP E': 45040, 'CLAVE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NOMBRE DEL USUARIO QUE REPORTA EL CREDITO': None, 'NUMERO CREDITO VIGENTE': None, 'TIPO DE RESPONSABILIDAD': 'I', 'TIPO DE CREDITO ': 'P', 'TIPO DE PRODUCTO': 'AR', 'MONEDA': 'MX', 'FRECUENCIA DE PAGO': 'M', 'MONTO DE PAGO': 80000, 'FECHA DE APERTURA': 20211206, 'FECHA DE ULTIMO PAGO': 20220825, 'MONTO DEL CREDITO A LA ORIGINACION': 2000000, 'PLAZO EN MESES': 24, 'FECHA DE LA ULTIMA DISPOSICION O COMPRA': 20211206, 'FECHA DEL REPORTE ACTUALIZACION O CORTE': 20230113, 'CREDITO MAXIMO UTILIZADO': 2000000, 'SALDO ACTUAL': 2000000, 'SALDO VENCIDO ': 583878.5893709798, 'FORMA DE PAGO O PAGO ACTUAL': 7, 'FECHA DEL PRIMER INCUMPLIMIENTO': 20220306, 'SALDO INSOLUTO DEL PRINCIPAL': 2000000, 'MONTO DEL ULTIMO PAGO': 28501.87}


acreditor_keys =['RFC', 'Nombres', 'ApellidoPaterno', 'ApellidoMaterno', 'FechaNacimiento', 'Direccion', 'ColoniaPoblacional', 'DelegacionMunicipio', 'Ciudad', 'Estado', 'CP', 'NombreEmpresa', 'Direccion E', 'ColoniaPoblacion E', 'DelegacionMunicipal E', 'Ciudad E', 'Estado E', 'CP E', 'ClaveActualOtorgante', 'NombreOtorgante', 'CuentaActual', 'TipoResponsabilidad', 'TipoCuenta', 'TipoContrato', 'ClaveUnidadMonetaria', 'FrecuenciaPagos', 'MontoPagar', 'FechaAperturaCuenta', 'FechaUltimoPago', 'FechaUltimaCompra', 'FechaCorte', 'CreditoMaximo', 'SaldoActual', 'Limite credito', 'SaldoVencido', 'PagoActual', 'FechaPrimerIncumplimiento', 'SaldoInsoluto', 'MontoUltimoPago', 'PlazoMeses', 'MontoCreditoOriginacion']

for i,key in enumerate(acreditor_keys): 
    print(f"{i+1} \t {key}")
    
print( list(acreditante_1.keys())[22:])