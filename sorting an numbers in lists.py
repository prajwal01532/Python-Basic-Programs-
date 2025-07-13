numbers=[21,12,3,34,15,36,17,80]
print("Printing numbers in acending Order:")
numbers.sort()
print(numbers)

print("Printing numbers in decending Order:")
numbers.reverse()
print(numbers)

print("Copy of numbers :")
num=numbers.copy()
numbers.append(2)
print(num)#2 is not appended in num