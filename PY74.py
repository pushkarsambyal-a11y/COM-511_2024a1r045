# 7. Write a Python program to store multiple student records as a list of tuples. Each tuple should contain name, roll number, and marks. Display students who scored above 75.

students = [
    ("Rahul", 101, 85),
    ("Aman", 102, 72),
    ("Priya", 103, 91),
    ("Riya", 104, 68),
    ("Karan", 105, 79)
]

print("Students who scored above 75:")

for student in students:
    name, roll, marks = student

    if marks > 75:
        print("Name:", name)
        print("Roll Number:", roll)
        print("Marks:", marks)
        print()