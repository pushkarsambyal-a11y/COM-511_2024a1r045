# 6. Write a Python program to store one student data as a tuple: name, roll number, and marks. Display grade based on marks.

student = ("Rahul", 101, 85)

name, roll, marks = student

print("Name:", name)
print("Roll Number:", roll)
print("Marks:", marks)

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)