# 6. Rotate a list one position to the right

numbers = list(map(int, input("Enter numbers: ").split()))

last = numbers[-1]

numbers.remove(last)
numbers.insert(0, last)

print("Rotated list:", numbers)