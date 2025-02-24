## ------ Ejercicio 4: Generador de contraseñas ------
import random
def Class(n):
    if n==0 or n==1:
        return 0
    elif n==2 or n%11==0:
        return 1
    else:
        for i in range(2,n):
            if n%i==0:
                return 2;break
            elif i==n-1 and n%i!=0:
                return 3
def Psw(l):
    sc="!","#","$","%","&","?","+","*","."
    abc="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
    ABC="A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    psw=""
    for i in range(l):
        if Class(i)==0:
            a=random.choice(ABC);psw+=a
        elif Class(i)==1:
            a=random.choice(sc);psw+=a
        elif Class(i)==2:
            a=str(random.randint(0,9));psw+=a
        else:
            a=random.choice(abc);psw+=a
    return psw
lgth=float(input("Type the length of the password: --- "))
while lgth<8 or int(lgth)!=lgth:
    lgth=float(input("ERROR: Invalid Input, please try again...\nType the length of the password: --- "))
force=input("Type a character that you want to force in the password: --- ")
while len(force)!=1 and len(force)!=0:
    force=input("ERROR: Invalid Input, please try again...\nType a character that you want to force in the password: --- ")
exclude=input("Type a character that you want to exclude from the password: --- ")
while len(exclude)!=1 and len(exclude)!=0:
    exclude=input("ERROR: Invalid Input, please try again...\nType a character that you want to force in the password: --- ")
psw=Psw(int(lgth))
while not(force in psw) or (exclude in psw):
    psw=Psw(int(lgth))
print(f"The password is: {psw}")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423
