# Q1. Create a Student class to store a student's name and roll number.
# Create an object and display the details using an instance method.

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)


s1 = Student("Rahul", 101)
s1.display()