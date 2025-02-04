def AgregarEsts(nombres,apellidos):
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