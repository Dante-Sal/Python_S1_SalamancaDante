def MostrarMenu():
    print("\n ------- MENU DE ACCIONES -------\n")
    print("1. Ver estudiantes")
    print("2. Agregar estudiantes")
    print("3. Editar estudiantes")
    print("4. Eliminar estudiantes")
    print("5. Salir del programa\n")
def MostrarMenuEd():
    print("\n ------- MENU DE EDICIÓN -------\n")
    print("1. Editar primer nombre")
    print("2. Editar segundo nombre")
    print("3. Editar primer apellido")
    print("4. Editar segundo apellido")
def MostrarMenuEd1Nm():
    print("\n ------- MENU DE EDICIÓN -------\n")
    print("1. Editar nombre")
    print("2. Editar primer apellido")
    print("3. Editar segundo apellido")
def MostrarEsts(nombres,apellidos):
    print("\n ------- LISTA DE ESTUDIANTES -------\n")
    for i in range(len(nombres)):
        if len(nombres[i])==1:
            print(f"Estudiante {i+1}: {nombres[i][0]} ",end="")
        else:
            print(f"Estudiante {i+1}: {nombres[i][0]} {nombres[i][1]} ",end="")
        print(f"{apellidos[i][0]} {apellidos[i][1]}")
nombres=[
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]
apellidos=[
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Roman", "Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
print("Bienvenido al programa de lista de estudiantes...")
r=True
while r==True:
    MostrarMenu()
    opc=input("Escribir : --- ")
    while opc!="1" and opc!="2" and opc!="3" and opc!="4" and opc!="5":
        print("\nERROR: Entrada inválida, por favor intente nuevamente...")
        MostrarMenu()
        opc=input("Escribir : --- ")
    if opc=="1":
        MostrarEsts(nombres,apellidos)
    elif opc=="2":
        est1Nm=input("\nIngrese el primer nombre del estudiante a insertar: ")
        est2Nm=input("Ingrese el segundo nombre del estudiante a insertar (en caso de no aplicar, presionar Enter): ")
        est1Ap=input("Ingrese el primer apellido del estudiante a insertar: ")
        est2Ap=input("Ingrese el segundo apellido del estudiante a insertar: ")
        if est2Nm!="":
            nvEstNm=[est1Nm,est2Nm]
        else:
            nvEstNm=[est1Nm]
        nvEstAp=[est1Ap,est2Ap]
        nombres.append(nvEstNm)
        apellidos.append(nvEstAp)
    elif opc=="3":
        MostrarEsts(nombres,apellidos)
        est=float(input("\nIngrese el número del estudiante a editar: "))
        while est<1 or est>len(nombres) or int(est)!=est:
            print("\nERROR: Entrada inválida, por favor intente nuevamente...")
            est=float(input("\nIngrese el número del estudiante a editar: "))
        if len(nombres[int(est)-1])==1:
            MostrarMenuEd1Nm()
            opcEd=input("\nEscribir : --- ")
            while opcEd!="1" and opcEd!="2" and opcEd!="3":
                print("\nERROR: Entrada inválida, por favor intente nuevamente...")
                MostrarMenuEd1Nm()
                opcEd=input("\nEscribir : --- ")
            if opcEd=="1":
                nombres[int(est)-1][0]=input(f"\nIngrese el nuevo nombre del estudiante {int(est)}: ")
            elif opcEd=="2":
                apellidos[int(est)-1][0]=input(f"\nIngrese el nuevo primer apellido del estudiante {int(est)}: ")
            else:
                apellidos[int(est)-1][1]=input(f"\nIngrese el nuevo segundo apellido del estudiante {int(est)}: ")
        else:
            MostrarMenuEd()
            opcEd=input("\nEscribir : --- ")
            while opcEd!="1" and opcEd!="2" and opcEd!="3" and opcEd!="4":
                print("\nERROR: Entrada inválida, por favor intente nuevamente...")
                MostrarMenuEd()
                opcEd=input("\nEscribir : --- ")
            if opcEd=="1":
                nombres[int(est)-1][0]=input(f"\nIngrese el nuevo primer nombre del estudiante {int(est)}: ")
            elif opcEd=="2":
                nombres[int(est)-1][1]=input(f"\nIngrese el nuevo segundo nombre del estudiante {int(est)}: ")
            elif opcEd=="3":
                apellidos[int(est)-1][0]=input(f"\nIngrese el nuevo primer apellido del estudiante {int(est)}: ")
            else:
                apellidos[int(est)-1][1]=input(f"\nIngrese el nuevo segundo apellido del estudiante {int(est)}: ")
    elif opc=="4":
        MostrarEsts(nombres,apellidos)
        est=float(input("\nIngrese el número del estudiante a eliminar: "))
        while est<1 or est>len(nombres) or int(est)!=est:
            print("\nERROR: Entrada inválida, por favor intente nuevamente...")
            est=float(input("\nIngrese el número del estudiante a eliminar: "))
        nombres.pop(int(est)-1)
        apellidos.pop(int(est)-1)
    elif opc=="5":
        r=False