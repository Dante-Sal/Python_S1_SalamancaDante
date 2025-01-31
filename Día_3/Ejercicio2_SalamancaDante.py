## ------ Ejercicio 2: Calculadora de interés simple y compuesto ------
def Int(p,r,t,n):
    s,c=round(p*(r/100)*t,2),round((p*((1+(r/100)/n)**(t*n)))-p,2)
    return s,c
x=input("Simple Interest (Type S);\nCompound Interest (Type C);\nType: --- ").upper()
while x!="S" and x!="C":
    x=input("\nERROR: Invalid Input, please try again...\nSimple Interest (Type S);\nCompound Interest (Type C);\nType: --- ").upper()
if x=="S":
    p=float(input("\nType the starting amount of money in dollars (principal): --- "))
    r=float(input("Type the percentage of the interest charged per year on the principal amount (rate): --- "))
    t=float(input("Type the number of years during which the principal is invested or borrowed (time): --- "))
    while p<=0 or r<=0 or t<=0:
        p=float(input("\nERROR: Invalid Input, please try again...\nType the starting amount of money in dollars (principal): --- "))
        r=float(input("Type the percentage of the interest charged per year on the principal amount (rate): --- "))
        t=float(input("Type the number of years during which the principal is invested or borrowed (time): --- "))
    print(f"The interest is ${Int(p,r,t,1)[0]}")
else:
    p=float(input("\nType the starting amount of money in dollars (principal): --- "))
    r=float(input("Type the percentage of the interest charged per year on the principal amount (rate): --- "))
    t=float(input("Type the number of years during which the principal is invested or borrowed (time): --- "))
    n=float(input("Type the number of compounding periods per year: --- "))
    while p<=0 or r<=0 or t<=0 or n<=0:
        p=float(input("\nERROR: Invalid Input, please try again...\nType the starting amount of money in dollars (principal): --- "))
        r=float(input("Type the percentage of the interest charged per year on the principal amount (rate): --- "))
        t=float(input("Type the number of years during which the principal is invested or borrowed (time): --- "))
        n=float(input("Type the number of compounding periods per year: --- "))
    print(f"The interest is ${Int(p,r,t,n)[1]}")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423