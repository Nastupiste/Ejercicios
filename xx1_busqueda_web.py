#Quiero hacer un contador de palabras claves en <<www.eldiario.es>>.

import urllib.request
webUrl = urllib.request.urlopen("https://www.eldiario.es/")
data = webUrl.read() 
data = str(data)
busqueda = input("Buscar palabra clave en www.diario.es:")
busquedaMayusculas = busqueda.upper()
numeroOcurrencias = busquedaMayusculas.count(busquedaMayusculas)
print ("El texto",busqueda, "ha aparecido", data.count(busqueda), "veces")
