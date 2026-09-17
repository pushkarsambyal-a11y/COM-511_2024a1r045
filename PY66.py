# 8. Count how many times an element appears in a list

numbers = list(map(int, input("Enter numbers: ").split()))

element = int(input("Enter element to search: "))

count = numbers.count(element)

print("Element appears", count, "times")