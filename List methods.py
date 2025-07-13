#lists methods
print('Append at last:')
numbers=[1,2,2,2,3,4,5,6]
numbers.append(20)
print(numbers)

print("Insert into index Examples:")
numbers.insert(1,80)
print(numbers)

print("Remove number from numbers Examples:")
numbers.remove(80)
print(numbers)

print(80 in numbers)#True or False if exists print True

print("Number of 2's in numbers")
print(numbers.count(2))#counts times of 2 in numbers

print("Pop last number from numbers Examples:")
numbers.pop()
print(numbers)

print("Clear all numbers from the numbers:")
numbers.clear()
print(numbers)
