numbers=[2,4,3,3,2,1]
no_duplicate=[]

for number in numbers:
    if number not in no_duplicate:
        no_duplicate.append(number)
print(no_duplicate)