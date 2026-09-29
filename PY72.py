# 5. Write a Python program to check whether a given value is present in a tuple. If present, display its position.

numbers = (10, 20, 30, 40, 50)

n = int(input("Enter value to search: "))

if n in numbers:
    print("Value is present")
    print("Position:", numbers.index(n) + 1)
else:
    print("Value is not present")