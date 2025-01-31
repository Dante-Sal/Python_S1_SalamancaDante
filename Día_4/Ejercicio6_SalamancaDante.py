## ------ Ejercicio 6: Secuencia de Fibonacci ------
def Fibcc(n,select,s):
    i=0
    a=0
    b=1
    sum=0
    if select=="A":
        print(f"\nThe Fibonacci sequence to term #{n} is: ",end="")
        if n==0:
            print(None)
        else:
            for i in range(n):
                if i==n-1:
                    print(a)
                else:
                    print(f"{a},",end="")
                c=a+b
                a=b
                b=c
    elif select=="E":
        print(f"\nThe Fibonacci sequence to term #{n} (only even numbers) is: ",end="")
        while i<n:
            if a%2==0:
                if i==n-1:
                    print(a)
                else:
                    print(f"{a},",end="")
                i+=1
            c=a+b
            a=b
            b=c
    elif select=="O":
        print(f"\nThe Fibonacci sequence to term #{n} (only odd numbers) is: ",end="")
        while i<n:
            if a%2==1:
                if i==n-1:
                    print(a)
                else:
                    print(f"{a},",end="")
                i+=1
            c=a+b
            a=b
            b=c
    else:
        print(f"\nThe Fibonacci sequence from term #{s} to term #{n} is: ",end="")
        for i in range(s-1):
            c=a+b
            a=b
            b=c
        for i in range(s,n+1):
            sum+=a
            if i==n:
                print(a)
            else:
                print(f"{a},",end="")
            c=a+b
            a=b
            b=c
        print(f"The sum of these terms is: {sum}")
x=input("Generate Fibonacci sequence (Type A);\nGenerate Fibonacci even numbers (Type E);\nGenerate Fibonacci odd numbers (Type O);\nCalculate the sum of Fibonacci numbers within a specified range (Type S);\nType: --- ").upper()
while x!="A" and x!="E" and x!="O" and x!="S":
    x=input("\nERROR: Invalid Input, please try again...\nGenerate Fibonacci sequence (Type A);\nGenerate Fibonacci even numbers (Type E);\nGenerate Fibonacci odd numbers (Type O);\nCalculate the sum of Fibonacci numbers within a specified range (Type S);\nType: --- ").upper()
if x=="S":
    s=float(input("\nType the position of the first number of the range: --- "))
    n=float(input("Type the position of the last number of the range: --- "))
    while int(s)!=s or s<0 or int(n)!=n or n<0:
        s=float(input("\nERROR: The Input must not contain decimals or be negative, please try again...\nType the position of the first number of the range: --- "))
        n=float(input("Type the position of the last number of the range: --- "))
        while n<s:
            s=float(input("\nERROR: The last number cannot be less than the first number, please try again...\nType the position of the first number of the range: --- "))
            n=float(input("Type the position of the last number of the range: --- "))
    Fibcc(int(n),x,int(s))
else:
    n=float(input("\nType the amount of Fibonacci numbers to display: --- "))
    while int(n)!=n or n<0:
        n=float(input("\nERROR: The Input must not contain decimals or be negative, please try again...\nType the amount of Fibonacci numbers to display: --- "))
    Fibcc(int(n),x,0)
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423