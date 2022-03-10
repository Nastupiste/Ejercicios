


empresa=[]

dpto1=["informatica"]
dpto2=["Recursos Humanos"]

empleado_1=["Juan","tecnico"]
empleado_2=["Marta","Jefa"]
empleado_3=["pepe","secretario"]
empleado_4=["Isma","Vicepresidente"]
empleado_5=["Lola","Ceo"]

empleados_dpto1=[empleado_1,empleado_2]
empleados_dpto2=[empleado_3,empleado_4,empleado_5]

dpto1.append(empleados_dpto1)
dpto2.append(empleados_dpto2)

empresa.append(dpto1)
empresa.append(dpto2)

for departamento in empresa:
    print("DEPARTAMENTO:",departamento[0])
    for empleado in departamento[1]:
        print("--Empleado:",empleado[0])
        print("--categoria:",empleado[1])
