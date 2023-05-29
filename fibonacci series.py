a, b = 0, 1
n = int(input("ENTER NO:"))
while b < n:
    print(b, end=" ")
    a, b = b, a+b
