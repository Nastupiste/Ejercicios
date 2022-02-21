frase = "En un lugar de La Mancha, La Mancha es una región"
fraseMayusculas = frase.upper()
textfinder = input("Introduzca el texto a buscar:")
textfinderMayusculas = textfinder.upper()
numeroOcurrencias = fraseMayusculas.count(textfinderMayusculas)
print ("El texto",textfinder, "ha aparecido", numeroOcurrencias, "veces")

