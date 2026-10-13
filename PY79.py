# 6. Write a program to reverse every kth row in a matrix.

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)

k = int(input("Enter k: "))

for i in range(0, rows, k):
    matrix[i].reverse()

print("Matrix after reversing every kth row:")

for row in matrix:
    print(row)