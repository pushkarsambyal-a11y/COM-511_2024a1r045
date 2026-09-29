# 4. Write a Python program to store repeated values in a tuple and count how many times a given value appears.

numbers = (10, 20, 10, 30, 20, 10, 40, 10)

n = int(input("Enter value to count: "))

count = numbers.count(n)

print("Number of times", n, "appears:", count)