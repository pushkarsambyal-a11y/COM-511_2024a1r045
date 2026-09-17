# 1. Display highest, lowest, average marks and number of passed students

n = int(input("Enter number of students: "))

marks = []

for i in range(n):
    mark = int(input("Enter marks: "))
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / n

passed = 0

for mark in marks:
    if mark >= 40:
        passed += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Number of students passed:", passed)