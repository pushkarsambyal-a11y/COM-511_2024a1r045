# 3. Write a Python program to show that tuple values cannot be changed directly. Convert tuple into list, update it, and convert it back into tuple.

numbers = (10, 20, 30, 40)

print("Original tuple:", numbers)

# Tuple cannot be changed directly
# numbers[1] = 50

numbers = list(numbers)

numbers[1] = 50

numbers = tuple(numbers)

print("Updated tuple:", numbers)