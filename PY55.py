# WAP to print an inverted right angles triangle

n = int(input("Enter the number of rows and cols : "))

for i in range(n , 0, -1):
    for j in range(1, i + 1):
        print("*", end = (" "))
    print()