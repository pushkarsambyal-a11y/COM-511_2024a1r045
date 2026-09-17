# 3. Find the second largest number in a list

numbers = list(map(int, input("Enter numbers: ").split()))

numbers.sort()

print("Second largest number:", numbers[-2])