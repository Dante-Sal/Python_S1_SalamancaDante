def MostrarEsts(nombres,apellidos):
    print("\n ------- LISTA DE ESTUDIANTES -------\n")
    for i in range(len(nombres)):
        if len(nombres[i])==1:
            print(f"Estudiante {i+1}: {nombres[i][0]} ",end="")
        else:
            print(f"Estudiante {i+1}: {nombres[i][0]} {nombres[i][1]} ",end="")
        print(f"{apellidos[i][0]} {apellidos[i][1]}")