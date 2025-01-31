## ------ Ejercicio 3: Clasificador de números ------
def Class(n):
    if n%2==0:
        print("[The number is even]")
    else:
        print("[The number is odd]")
    if n==0 or n==1:
        print("[The number is neither prime nor composite]")
    elif n==2:
        print("[The number is prime]")
    else:
        for i in range(2,n):
            if n%i==0:
                print("[The number is composite]");break
            elif i==n-1 and n%i!=0:
                print("[The number is prime]")
    if n**0.5-int(n**0.5)==0:
        print("[The number is a perfect square]")
    else:
        print("[The number is not a perfect square]")
n=float(input("Type a number: --- "))
while int(n)!=n or n<0:
    n=float(input("ERROR: The Input must not contain decimals or be negative, please try again...\nType a number: --- "))
Class(int(n))
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423