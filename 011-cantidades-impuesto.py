#Solicitar al usuario dos cantidades (dos importes)
#Solicitar al usuario el porcentaje de impuestos (IVA)
#Mostrar el importe de la factura (i1+i2 + impuesto)
importe1 = float (input("Introduce el valor del primer importe:"))
importe2 = float (input("Introduce el valor del segundo importe:"))
IVA = float(input("¿Cuanto IVA tienes que pagar?:"))/100
importeFactura = (importe1+importe2)+(importe1+importe2)*IVA
print("Su factura total es", importeFactura, "euros")