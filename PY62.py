# 4. Create a new list containing only unique elements

numbers = list(map(int, input("Enter numbers: ").split()))

unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print("Unique elements:", unique)