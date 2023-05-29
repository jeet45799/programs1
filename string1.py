s=input("enter sring : ")
ch=0
nm=0
spc=0
up=0
lw=0
space=0
for i in s:
    if i.isalpha():
        ch=ch+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        space=space+1
    else:
        spc=spc+1
    if i.isupper():
        up=up+1
    if i.islower():
        lw=lw+1
print("character :",ch)
print("number :",nm)
print("space :",spc)
print("uppercase :",up)
print("lowercase :",lw)
print("space :",space)
