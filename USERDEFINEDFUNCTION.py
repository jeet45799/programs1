#FUNCTION WITH NO ARGUMENT & NO RETURN VALUE

def printline():
    print("*"*50)
printline()
print("welcome to python")
printline()

#FUNCTION WITH ARGUMENT BUT NO RETURN VALUE

def add(a,b):
    print("addition :",a+b)
printline()
x=int(input("enter value:"))
y=int(input("enter value:"))
add(x,y)
printline()

#FUNCTION WITH ARGUMENT AND RETURN VALUE

def sub(a,b):
    return a-b
printline()
x=int(input("enter no :"))
y=int(input("enter no :"))
ans=sub(x,y)
print("subtraction :",ans)
printline()
