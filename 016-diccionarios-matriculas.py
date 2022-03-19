#Crear un diccionario con tres vehiculos. Pedimos al usario una matricula y mostramos: (los datos o decimos que no existe.)
#-Clave: matricula
#-Valor: marca, modelo y color

base_datos={}
base_datos["1111 AAA"]=["Renault","Laguna","Blanco"]
base_datos["1112 AAA"]=["Toyota","Auris","Gris"]
base_datos["1113 AAA"]=["Seat","Leon","Azul"]
busqueda=input("Intoduzca matricula del vehiculo:")
if busqueda in base_datos:
    print(base_datos[busqueda])
else:
    print("Lo sentimos, su matricula no está en la base de datos.")