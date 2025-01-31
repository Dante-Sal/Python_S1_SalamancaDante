## ------ Ejercicio 5: Número faltante en la serie ------
a=1
b=1
for i in range(7):
    print(a)
    if i%2==0:
        c=a+b
    else:
        c=a-b
    a=b
    b=c
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423
    