'''
output should:
xxxxx
xx
xxxxx
xx
xx

'''
numbers=[5,2,5,2,2]
for x in numbers:
    output=''
    for y in range(x):
        output=output +'x'
    print(output)



