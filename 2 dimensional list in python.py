matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
#repalcing [0][1]
matrix[0][1]=5
print(matrix[0][1])
print(matrix)
#printing items in row
print("Items in Row:")
for row in matrix:
    for item in row:
        print(item)