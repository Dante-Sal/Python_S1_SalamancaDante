from MostrarMenuEd import *
from MostrarMenuEd1Nm import *
from MostrarEsts import *
from Verificaciones import *
def EditarEsts(nombres,apellidos):
    MostrarEsts(nombres,apellidos)
    est=float(input("\nIngrese el número del estudiante a editar: "))
    est=VerificacionEST(est,nombres)
    if len(nombres[int(est)-1])==1:
        MostrarMenuEd1Nm()
        opcEd=input("\nEscribir : --- ")
        VerificacionOPCED1Nm(opcEd)
        if opcEd=="1":
            nombres[int(est)-1][0]=input(f"\nIngrese el nuevo nombre del estudiante {int(est)}: ")
        elif opcEd=="2":
            apellidos[int(est)-1][0]=input(f"\nIngrese el nuevo primer apellido del estudiante {int(est)}: ")
        else:
            apellidos[int(est)-1][1]=input(f"\nIngrese el nuevo segundo apellido del estudiante {int(est)}: ")
    else:
        MostrarMenuEd()
        opcEd=input("\nEscribir : --- ")
        VerificacionOPCED(opcEd)
        if opcEd=="1":
            nombres[int(est)-1][0]=input(f"\nIngrese el nuevo primer nombre del estudiante {int(est)}: ")
        elif opcEd=="2":
            nombres[int(est)-1][1]=input(f"\nIngrese el nuevo segundo nombre del estudiante {int(est)}: ")
        elif opcEd=="3":
            apellidos[int(est)-1][0]=input(f"\nIngrese el nuevo primer apellido del estudiante {int(est)}: ")
        else:
            apellidos[int(est)-1][1]=input(f"\nIngrese el nuevo segundo apellido del estudiante {int(est)}: ")
