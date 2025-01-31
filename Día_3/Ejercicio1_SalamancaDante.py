## ------ Ejercicio 1: Conversor de temperatura ------
def Temp(cls,fheit):
    f,c=round((cls*9/5)+32,2),round((fheit-32)*5/9,2)
    return f,c
x=input("Convert °C -> °F (Type C);\nConvert °F -> °C (Type F);\nType: --- ").upper()
while x!="C" and x!="F":
    x=input("\nERROR: Invalid Input, please try again...\nConvert °C -> °F (Type C);\nConvert °F -> °C (Type F);\nType: --- ").upper()
if x=="C":
    oc=float(input("\nType the number of degrees Celsius to convert to degrees Fahrenheit: --- "))
    while oc<-273.15:
        oc=float(input("ERROR: Invalid Input, please try again...\nType the number of degrees Celsius to convert to degrees Fahrenheit: --- "))
    print(f"{oc}°C equals {Temp(oc,0)[0]}°F")
else:
    of=float(input("\nType the number of degrees Fahrenheit to convert to degrees Celsius: --- "))
    while of<Temp(-273.15,0)[0]:
        of=float(input("ERROR: Invalid Input, please try again...\nType the number of degrees Fahrenheit to convert to degrees Celsius: --- "))
    print(f"{of}°F equals {Temp(0,of)[1]}°C")
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423
