#ejercicio operadores lógicos. Para contratar a una persona:
#Debe ser mayor de edad. Nacionalidad Frances o Aleman. 
#No ruso. 
#Debe daber Ingles y chino.
#Primero todas las preguntas y despues se decide.


print("Bienvenido a la entrevista de trabajo!")
print("Necesitamos que contestes a unas preguntas.")
MAYORIA_EDAD=18
edad = int(input("¿Qué edad tienes?:"))
nacionalidad = input("¿Cuál es tu nacionalidad?:")
idioma1 = input("¿Cuál es tu primer idioma?:")
idioma2 = input("¿Cuál es tu segundo idioma?:")


mayor_edad = edad>=MAYORIA_EDAD
nacionalidad_ok = (nacionalidad=="frances" or nacionalidad=="aleman") and nacionalidad!="ruso"
idiomas_ok = idioma1=="ingles" or "chino" and idioma2=="ingles" or "chino"
if (mayor_edad and nacionalidad_ok and idiomas_ok):
    print("Contratado!!!")
else:
    print("Lo sentimos, no cumple con el perfil....")