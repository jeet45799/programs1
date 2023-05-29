#1
str1="tops technologies"
rev_upper=lambda string: string.upper()[::-1]
print(rev_upper(str1))

#2
Max = lambda a, b : a if(a > b) else b
print(Max(1, 2))

#3
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)

#4
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences)
print(list(filtered_result))

#5
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences)
print(list(filtered_result))
