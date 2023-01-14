Buenas tardes Luis.


Te mando el email con algunas de las modificaciones que le realice al archivo en base a al manual de circulo de crédito.


aunque la mayor modificación o la mas sustancial se basa en como debe de estar estructurado el XML ya que la estructura de este y su sintaxis no permite la existencia de espacios, es preferible unir las palabras  de los títulos sin espacios como por ejemplo "ApellidoMaterno" en ves de "Apellido materno"


Una disculpa porque la mayoría de estos cambios fueron ocasionados por no leer detenidamente la información de los últimos anexos 


 - Algunos de los apartados que se mencionan en el manual están unidos como por ejemplo : las celdas primero y segundo nombre es mas conveniente que fueran una misma con el titulo de la columna como Nombres
- Según el manual de circulo de créditos se debería nombrar las columnas "código postal" como CP
- En el apartado de Empleo o actividad económica, debido a que es muy ineficiente la búsqueda de las celdas a través de una que se encuentra por encima de las mismas creo que es mejor darles un indicador al final del titulo como la letra E, así yo sabré identificar cuales columnas corresponden a el domicilio de la persona y al de la empresa donde trabaja.
- Dentro del aportado de crédito, realice algunos cambios a los títulos pues aunque yo establecí el nombre de las variables al leer el anexo B me di cuenta que se les asignan nombres distintos a las variables a la hora de transfórmalas en etiquetas XML esta es su nueva designación


 - Clave del Usuario que reporta el crédito : ClaveActualOtorgante
 - Nombre del Usuario que reporta el crédito : NombreOtorgante
 - Número Crédito Vigente : CuentaActual 
 - Tipo de Responsabilidad : TipoResponsabilidad
 - Tipo de Crédito : TipoCuenta
 - Tipo de Producto : TipoContrato
 - Moneda : ClaveUnidadMonetaria
 - Frecuencia de Pago : FrecuenciaPagos
 - Monto de Pago : MontoPagar
 - Fecha de Apertura : FechaAperturaCuenta
 - Fecha del Último Pago : FechaUltimoPago
 -  Fecha de la Última Disposición o Compra : FechaUltimaCompra
 -  Fecha del reporte, Actualización o Corte : FechaCorte
 - Crédito Máximo Utilizado : CreditoMaximo
 - Saldo Actual : SaldoActual 
 - LimiteCredito (nuevo) : Cantidad máxima concedida por el Usuario. Es obligatorio para créditos revolventes y el monto debe ser el mismo que se notifica en el estado de cuenta.  (aunque nosotros no tengamos créditos revolventes puedes poner el apartado ya que no se si es o no obligatorio establecerlo.
 - Saldo Vencido : SaldoVencido
 - Forma de Pago o Pago Actual : PagoActual
 - Fecha del Primer Incumplimiento : FechaPrimerIncumplimiento
 - Saldo Insoluto del Principal : SaldoInsoluto
 - Monto del Último Pago : MontoUltimoPago
 - Plazo en Meses : PlazoMeses
 -  Monto del Crédito a la Originación : MontoCreditoOriginacion  