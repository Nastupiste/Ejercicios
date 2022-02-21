def age(edad):
    if edad>=18:
        print("¡Enhorabuena puedes beber alcohol!")
    else:
        print("¡Lo siento!No puedo venderte alcohol")
print("Hola, necesito saber si eres mayor de edad.")
edad=input("¿Cuántos años tienes?")
edad=int(edad)
age(edad)
