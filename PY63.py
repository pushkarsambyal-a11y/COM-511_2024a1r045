# 5. Create separate lists for even and odd numbers

numbers = list(map(int, input("Enter numbers: ").split()))

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)