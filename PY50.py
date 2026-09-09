# Write a Python program to print numbers from 1 to 50, but skip all numbers divisible by 4

for num in range(1, 51):
    if num % 4 == 0:
        continue
    print(num)