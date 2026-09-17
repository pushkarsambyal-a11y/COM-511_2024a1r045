# 2. Store only valid marks between 0 and 100

marks = []

for i in range(10):
    mark = int(input("Enter marks: "))

    if mark >= 0 and mark <= 100:
        marks.append(mark)

print("Valid marks:", marks)