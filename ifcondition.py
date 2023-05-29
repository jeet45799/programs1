a=int(input("enter A:"))
if a>0:
    print("A is positive")
else:
    print("A is negative")

#EVEN AND ODD
a=int(input("enter A:"))
if a%2==0:
    print("A is EVEN")
else:
    print("A is ODD")
#MAX NUMBER
a=int(input("enter A:"))
b=int(input("enter B:"))
if a>b:
    print("A is max")
else:
    print("B is max")
#3 MAX COMPARISON
a=int(input("ENTER A:"))
b=int(input("ENTER B:"))
c=int(input("ENTER C:"))
if a>b:
    if a>c:
        print("A IS MAX")
    else:
        print("C IS MAX")
elif b>c:
    print("B IS MAX")
else:
    print("C IS MAX")
