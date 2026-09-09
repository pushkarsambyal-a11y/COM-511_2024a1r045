# Write a Python program to repeatedly calculate the sum of digits of a number until the result becomes a single digit.

# Example: 9875 ->9+8+7+5 = 29 -> 2+9= 11 -> 1+ 1 = 2

number = int(input("Enter a number: "))
while number >= 10:
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number //= 10
    number = digit_sum

print(f"The single-digit sum is: {number}")