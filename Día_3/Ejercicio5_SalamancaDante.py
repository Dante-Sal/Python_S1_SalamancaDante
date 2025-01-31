## ------ Ejercicio 5: Detector de palíndromos ------
import re
def Format(txt):
    txt=txt.lower()
    nwTxt=re.sub(r"\W|_","",txt)
    nwTxt=nwTxt.replace("á","a");nwTxt=nwTxt.replace("é","e")
    nwTxt=nwTxt.replace("í","i");nwTxt=nwTxt.replace("ó","o")
    nwTxt=nwTxt.replace("ú","u");nwTxt=nwTxt.replace("ü","u")
    return nwTxt
def Rev(txt):
    rvTxt=""
    nwTxt=Format(txt)
    for c in nwTxt:
        rvTxt=c+rvTxt
    return rvTxt
def Pld(phr):
    if Format(phr)==Rev(phr):
        print("[The string is a palindrome]")
    else:
        print("[The string is not a palindrome]")
phr=input("Type a phrase: --- ")
Pld(phr)
## Desarrollado por : Dante Salamanca / T.I.: 1.097.498.423