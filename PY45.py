# Write a Python program to input a number and check whether it is prime or not.
#  A number is prime if it has no divisor other than 1 and itself.

number = int(input("Enter a number: "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")