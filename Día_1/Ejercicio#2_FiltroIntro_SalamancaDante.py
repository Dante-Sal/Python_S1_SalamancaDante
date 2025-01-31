## ------ Ejercicio 2: Sumatoria de la serie numérica 1 - 1/2 + 1/3 - 1/4 + ... +- 1/N ------
print("Ingrese la cantidad de términos que desee: ",end="")
N=int(input())
sum=0

for i in range(1,N+1):
    if i%2==1:
        sum+=1/i
    else:
        sum-=1/i
    
print(f"""La cantidad de términos es: {N}
El resultado de la operacion es: {sum}""")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423