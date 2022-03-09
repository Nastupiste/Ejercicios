#Descargar el qijote del enlace: https://www.gutenberg.org/files/2000/2000-0.txt
#Convertir el texto a string
#Guardarlo en una lista (utilizando split)
#Pedimos al usuario una palabra y le vamos a decir cuantas veces aparece la palabra en el libro.
#Se pueden usar independientemente mayúsculas y minúsculas. 

#primer paso
import urllib.request
print("leyendo URL")
webUrl = urllib.request.urlopen("https://www.gutenberg.org/files/2000/2000-0.txt")
quijote_bruto = webUrl.read() 
#segundo paso
quijote_bruto = str(quijote_bruto)
texto_mayuscula = quijote_bruto.upper()
#tercer paso
print("obteniendo la lista de palabras")
lista_palabras = texto_mayuscula.split()
#cuarto punto
palabra_clave = input("Introduce la palabra a buscar:")
numero_apariciones = texto_mayuscula.count(palabra_clave.upper())
print("la palabra" ,palabra_clave,"ha apareceido", numero_apariciones,"veces en el Quijote.")
#quinto punto
if palabra_clave.upper() in lista_palabras:
    print(palabra_clave, "existe en el Quijote")
else: 
    print(palabra_clave, "no existe en el Quijote")