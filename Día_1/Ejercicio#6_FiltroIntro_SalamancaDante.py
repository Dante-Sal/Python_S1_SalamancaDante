## ------ Ejercicio 6: Empresa ACME ------
totalBruto=0
totalDescuento=0
totalNeto=0
print("Ingrese la cantidad de empleados: ",end="")
N=int(input())
for i in range(N):
    print(f"\nIngrese el nombre del empleado {i+1}: ",end="")
    nombre=input()
    print(f"Ingrese las horas trabajadas por el empleado {i+1}: ",end="")
    horas=float(input())
    sueldoBruto=20000*horas
    descuento=sueldoBruto*0.04
    sueldoNeto=sueldoBruto-descuento*2
    totalBruto+=sueldoBruto
    totalDescuento+=descuento
    totalNeto+=sueldoNeto
    print(f"""
Empleado {i+1}: {nombre}
    Sueldo bruto: ${sueldoBruto}
    Descuento EPS: ${descuento}
    Descuento pensión: ${descuento}
    Sueldo neto: ${sueldoNeto}""")
    if i==0:
        nombreMax=nombre
        nombreMin=nombre
        sueldoMax=sueldoNeto
        sueldoMin=sueldoNeto
    elif sueldoNeto>sueldoMax:
        nombreMax=nombre
        sueldoMax=sueldoNeto
    elif sueldoNeto<sueldoMin:
        nombreMin=nombre
        sueldoMin=sueldoNeto
promedioBruto=totalBruto/N
promedioNeto=totalNeto/N
print(f"""
Total salarios brutos: ${totalBruto}
Total descuentos EPS: ${totalDescuento}
Total descuentos pensión: ${totalDescuento}
Total salarios netos: ${totalNeto}

Empleado que más gana: {nombreMax}
    Salario neto: ${sueldoMax}

Empleado que menos gana: {nombreMin}
    Salario neto: ${sueldoMin}

Promedio salarios brutos: ${promedioBruto}
Promedio salarios netos: ${promedioNeto}""")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423