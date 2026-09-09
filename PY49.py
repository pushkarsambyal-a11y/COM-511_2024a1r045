# Write a Python program to input a decimal number and convert it into binary without using the built-in bin() function.

decimal_number = int(input("Enter a decimal number: "))
binary_number = ""

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + binary_number
    decimal_number = decimal_number // 2

print(f"The binary representation is: {binary_number}")