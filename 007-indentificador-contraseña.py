PALABRA_PROHIBIDA1 = "ADMIN"
PALABRA_PROHIBIDA2 = "123"
PALABRA_PROHIBIDA3 = "PASSWORD"

idUsuario = input ("Introduzca su usuario:")
pwd = input ("Introduzca su contraseña:")

if pwd.count(PALABRA_PROHIBIDA1)==0:
    if pwd.count(PALABRA_PROHIBIDA2)==0:
        if pwd.count(PALABRA_PROHIBIDA3)==0:
            print("la password es correcta")
        else:
            print("error")
    else:
        print("error")
else:
    print("error")              