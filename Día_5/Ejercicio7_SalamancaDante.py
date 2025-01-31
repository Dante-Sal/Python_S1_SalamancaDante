def Fact(n):
    x=1
    for i in range(1,n+1):
        x*=i
    return x
def Cmb(n,select,k):
    if select=="P":
        x=Fact(n)/Fact(n-k)
    elif select=="PR":
        x=n**k
    elif select=="C":
        x=Fact(n)/(Fact(k)*Fact(n-k))
    else:
        x=Fact(n+k-1)/(Fact(k)*Fact(n-1))
    return x
x=input("Calculate the factorial of a number (Type F);\nPermutation (Type P);\nCombination (Type C);\nPermutation with repetition (Type PR);\nCombination with repetition (Type CR);\nType: --- ").upper()
if x=="F":
    n=int(input("Type a number: --- "))
    print(f"The factorial of {n} is: {Fact(n)}")