n = int(input("ENTER NO:"))
if n % 2 != 0:
    for i in range(3, int(n/2)+1, 2):
        if n % i == 0:
            print("is not a prime number")
            break
    else:
        print("is a prime number")
else:
    print("is not prime")


