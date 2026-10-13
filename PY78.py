# 5. Write a program to perform searching activity using Linear and binary search.

numbers = list(map(int, input().split()))

target = int(input("Enter number to search: "))

# Linear Search
found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Linear Search: Element found at position", i + 1)
        found = True
        break

if found == False:
    print("Linear Search: Element not found")


# Binary Search
numbers.sort()
low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == target:
        print("Binary Search: Element found at position", mid + 1)
        found = True
        break
    elif target < numbers[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found == False:
    print("Binary Search: Element not found")