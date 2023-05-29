#1
List = [i for i in range(1,100) if i%2==0]
print(List)

#2
h_letters = [ letter for letter in 'human' ]
print( h_letters)

#3
num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)

#4
obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj)

#5
numbers = [3, 5, 1, 7, 3, 9]
num = [n**2 for n in numbers]
print(num)

#6
number_list = [ num for num in range(30) if num % 2 != 0]
print(number_list)

#7
names = ['Steve', 'Bill', 'Ram', 'Mohan', 'Abdul']
names2 = [s for s in names if 'a' in s]
print(names2)

#8
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums=[(x,y) for x in nums1 for y in nums2]
print(nums)

#9
a = [4,6,7,3,2]
b = [x for x in a if x > 5]
print(b)

#10
vals = [[1,2,3],[4,5,2],[3,2,6]]
vals_max = [max(x) for x in vals]
print(vals_max)
