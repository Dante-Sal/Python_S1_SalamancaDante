## ------ Ejercicio 4: Mayor y menor de 10 números ------
xMax=0
xMin=0
for i in range(10):
    print(f"Ingrese el número {i}: ",end="")
    x=int(input())
    if i==0:
        xMax=x
        xMin=x
    elif x>xMax:
        xMax=x
    elif x<xMin:
        xMin=x
print(f"""El número mayor es: {xMax}
El número menor es: {xMin}""")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423