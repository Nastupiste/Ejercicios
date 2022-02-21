#Ejercicio que pide: 
# Preguntar un salario anual. 
# Verificar si el salario es un número. 
# Verificar que el salario es positivo. 
# Pedir el numero de mensualidades (12/14).
# Mostrar salario Mensual'

from win10toast import ToastNotifier
salarioAnual = input("Hola. Introduce tu salario anual:")
if salarioAnual.isdigit():
    salarioAnual = int(salarioAnual)
    pagas = int(input("Introduce el número de pagas 12/14:"))
    salarioMensual = (salarioAnual / pagas)
    print("Tu salario mensual es ", salarioMensual, "euros en", pagas, "pagas")
    toaster = ToastNotifier()
    toaster.show_toast("Juanra Project","Tu salario mensual es"+string(mensual))
elif salarioAnual[0]=="-":
    print("El salario anual no puede ser negativo")
else: 
    print("El salario anual es erróneo")
