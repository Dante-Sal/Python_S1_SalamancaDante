from MostrarEsts import *
from Verificaciones import *
def EliminarEsts(nombres,apellidos):
    MostrarEsts(nombres,apellidos)
    est=float(input("\nIngrese el número del estudiante a eliminar: "))
    VerificacionEST(est,nombres)
    nombres.pop(int(est)-1)
    apellidos.pop(int(est)-1)