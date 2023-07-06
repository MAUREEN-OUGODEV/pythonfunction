names=["Mercy","Nancy","Regina","Susan","Marion","Ann","Lekishon"]
first,second,third,*rest = names
print(first)
print(second)
print(*rest)

#sort()
numbers=[23,45,67,89,12,56,67]
numbers.sort()
print(numbers)
# 
numbers.reverse()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

myList=[*range(10,20+1)]
print(myList)
print(numbers)
# del numbers[3]

# print(numbers)
# print(numbers[0])
numbers2=set(numbers)
print(numbers2)

# del(numbers())
# numbers.remove(67)
# print(numbers)