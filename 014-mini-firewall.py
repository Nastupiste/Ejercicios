#Cuando se detecten 3 veces la misma IP se incluye a la misma en una lista negra.
#A partir de entonces, cuando se introduzca esa misma IP se le muestra un mensaje de rechazo.

numero_intentos = 3
ip_salida = "0"
ip="-1"
lista_ip = []
black_list = []
while ip!=ip_salida:
    ip=input("Introduce una dirección IP:")
    if (ip in black_list):
        print("La dirección",ip,"está atacando mi sistema")
    else:    
        lista_ip.append(ip)
        print(lista_ip)
        if (lista_ip.count(ip)==numero_intentos):
            black_list.append(ip)
 

 



