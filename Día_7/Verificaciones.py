from MostrarMenu import *
from MostrarMenuEd import *
from MostrarMenuEd1Nm import *
def VerificacionOPC(opc):
    while opc!="1" and opc!="2" and opc!="3" and opc!="4" and opc!="5":
        print("\nERROR: Entrada inválida, por favor intente nuevamente...")
        MostrarMenu()
        opc=input("Escribir : --- ")
    return opc
def VerificacionEST(est,nombres):
    while est<1 or est>len(nombres) or int(est)!=est:
        print("\nERROR: Entrada inválida, por favor intente nuevamente...")
        est=float(input("\nIngrese el número del estudiante a editar: "))
    return est
def VerificacionOPCED1Nm(opcEd):
    while opcEd!="1" and opcEd!="2" and opcEd!="3":
        print("\nERROR: Entrada inválida, por favor intente nuevamente...")
        MostrarMenuEd1Nm()
        opcEd=input("\nEscribir : --- ")
def VerificacionOPCED(opcEd):
    while opcEd!="1" and opcEd!="2" and opcEd!="3" and opcEd!="4":
        print("\nERROR: Entrada inválida, por favor intente nuevamente...")
        MostrarMenuEd()
        opcEd=input("\nEscribir : --- ")