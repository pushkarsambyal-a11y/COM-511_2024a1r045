# 9. Create a third list containing common elements

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

common = []

for number in list1:
    if number in list2 and number not in common:
        common.append(number)

print("Common elements:", common)