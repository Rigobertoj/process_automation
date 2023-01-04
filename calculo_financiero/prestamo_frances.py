# import locale
# locale.setlocale(locale.LC_ALL, 'en_MX.UTF-8')

from getTIIE import Tasa_De_Interes_Anual

capital = 10000
tasa = Tasa_De_Interes_Anual()
plazo = 12

# funcion que me permite obtener el pago mensual de un prestamo frances
def prestamo_frances(capital : int, tasa : int, plazo : int):
  """
  
  """  
  tasa = tasa / 12
  pago_mensual = (capital * tasa ) / (1 - (1 + tasa)**-plazo)
  return pago_mensual

# funcion que me permite crear una tabla de amorizacion sobre el prestamo frances 
def tabla_amortizacion_frances(capital_inicial, tasa, plazo):
    pago_mensual = prestamo_frances(capital_inicial,tasa, plazo)
    print(f"""
capital {capital_inicial}
interes {tasa}
plazo   {plazo}
""")
    saldo = capital_inicial     
    print("""
Saldo | interes | capital | pago mensual | saldo insoluto    
""")
    for i in range(0, plazo): 
        interes = saldo*tasa/12
        capital = pago_mensual - interes
        saldo_insoluto = saldo - capital
        print(f"""
{saldo:.2f}  {interes:.2f}  {capital:.2f}  {pago_mensual:.2f}  {saldo_insoluto:.2f} mes {i+1}
________________________________________"""
            )
        saldo = saldo_insoluto


if __name__ == '__main__':
    tabla_amortizacion_frances(capital,tasa,plazo)