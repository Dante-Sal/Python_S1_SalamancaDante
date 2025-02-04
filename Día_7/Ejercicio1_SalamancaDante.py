## ------ Ejercicio: Lista de Estudiantes con Módulos ------
from Listas import *;from MostrarMenu import *;from MostrarEsts import *;from AgregarEsts import *;from EditarEsts import *;from EliminarEsts import *;from Verificaciones import *
print("Bienvenido al programa de lista de estudiantes...");r=True
while r==True:
    MostrarMenu();opc=input("Escribir : --- ");opc=VerificacionOPC(opc)
    if opc=="1":MostrarEsts(nombres,apellidos)
    elif opc=="2":AgregarEsts(nombres,apellidos)
    elif opc=="3":EditarEsts(nombres,apellidos)
    elif opc=="4":EliminarEsts(nombres,apellidos)
    elif opc=="5":r=False
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423