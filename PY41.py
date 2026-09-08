# Write a Python program to input marks of 5 students.
# For each student, the program should check whether the entered marks are valid or invalid. Marks are considered valid only if they are between 0 and 100.
# If the marks are invalid, the program should display "Invalid marks skipped" and move to the next student without printing those marks.
# If the marks are valid, the program should display the marks as valid.

marks = int(input("Enter marks of student 1: "))
if marks >= 0 and marks <= 100:
    print("Valid marks:", marks)
else:
    print("Invalid marks skipped")

marks = int(input("Enter marks of student 2: "))
if marks >= 0 and marks <= 100:
    print("Valid marks:", marks)
else:
    print("Invalid marks skipped")

marks = int(input("Enter marks of student 3: "))
if marks >= 0 and marks <= 100:
    print("Valid marks:", marks)
else:
    print("Invalid marks skipped")

marks = int(input("Enter marks of student 4: "))
if marks >= 0 and marks <= 100:
    print("Valid marks:", marks)
else:
    print("Invalid marks skipped")

marks = int(input("Enter marks of student 5: "))
if marks >= 0 and marks <= 100:
    print("Valid marks:", marks)
else:
    print("Invalid marks skipped")

