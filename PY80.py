# 7. Write a Python program to create records of n students. Store each student record as a dictionary containing roll number, name, branch, and marks. Store all records in a list and search for a student using roll number.
# Condition: Roll numbers must be unique.

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    roll = int(input("Enter roll number: "))

    # Check for unique roll number
    while True:
        duplicate = False

        for student in students:
            if student["roll"] == roll:
                duplicate = True
                break

        if duplicate:
            print("Roll number already exists. Enter a different roll number.")
            roll = int(input("Enter roll number: "))
        else:
            break

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

print("\nStudent Records:")

for student in students:
    print(student)

search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in students:
    if student["roll"] == search_roll:
        print("Student found:")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if found == False:
    print("Student not found")