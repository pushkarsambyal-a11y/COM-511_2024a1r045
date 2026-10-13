# 8. Create a database using lists and tuples. Each student record must contain roll number, name, branch, and CGPA. Store each record as a tuple inside a list. Display all records and search for a student using roll number.
# Conditions:
# - Each record should be stored as a tuple.
# - The complete database should be stored as a list.
# - Roll numbers must be unique.

n = int(input("Enter number of students: "))

database = []

for i in range(n):
    roll = int(input("Enter roll number: "))

    # Check for unique roll number
    while True:
        duplicate = False

        for student in database:
            if student[0] == roll:
                duplicate = True
                break

        if duplicate:
            print("Roll number already exists. Enter a different roll number.")
            roll = int(input("Enter roll number: "))
        else:
            break

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    cgpa = float(input("Enter CGPA: "))

    student = (roll, name, branch, cgpa)

    database.append(student)

print("\nStudent Database:")

for student in database:
    print(student)

search_roll = int(input("\nEnter roll number to search: "))

found = False

for student in database:
    if student[0] == search_roll:
        print("Student found:")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Branch:", student[2])
        print("CGPA:", student[3])
        found = True
        break

if found == False:
    print("Student not found")