## ------ Ejercicio 7: Números amigos ------
print("Ingrese dos números:\n")
n1=int(input("Número 1: "))
n2=int(input("Número 2: "))
sum1=0
sum2=0
for i in range(1,n1):
    if n1%i==0:
        sum1+=i
for i in range(1,n2):
    if n2%i==0:
        sum2+=i
if sum1==n2 and sum2==n1:
    print("Los números son amigos...")
else:
    print("Los números no son amigos...")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423