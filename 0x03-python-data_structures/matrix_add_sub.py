# get user input for row and column
row = int(input("Enter the row number: "))
col = int(input("Enter the column number: "))
print("Enter matrix1 elements:")

matrix1 = [[int(input()) for i in range(row)] for j in range(col)]
print("matrix1: ")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j], "<3"), end=" ")
    print()

print("Enter matrix2 elements: ")
matrix2 = [[int(input()) for m in range(row)] for n in range(col)]
print("matrix2: ")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j], "<3"), end=" ")
    print()

result = [[0 for i in range(row)] for j in range(col)]
for i in range(row):
    for j in range(col):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

print("Result is: ")
for i in range(row):
    for j in range(col):
        print(format(result[i][j], "<3"), end=" ")
    print()
