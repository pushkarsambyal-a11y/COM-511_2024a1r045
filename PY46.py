# Write a Python program to input two numbers and find their greatest common divisor using a loop and using euclidean algorithm.

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

while number2 != 0:
    temp = number2
    number2 = number1 % number2
    number1 = temp

print(f"The greatest common divisor is: {number1}")