# Write a python program to print the right angle triangle number pattern

n = int(input("Enter the number of rows and columns: "))

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
