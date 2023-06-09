def cube(x):
    return x*x*x
num=(5,7,9,11,13,34,67,78,90,877)
result=map(cube,num)
print(list(result))
