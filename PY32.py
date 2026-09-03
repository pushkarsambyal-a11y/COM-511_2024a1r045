# Take student full name and roll number. Generate email using first 3 letters of first name, 
# first 3 letters of last name, and last 3 characters of roll number.
name = input("Enter full name: ")
roll = input("Enter roll number: ")

first = name.split()[0]
last = name.split()[-1]

email = first[:3].lower() + last[:3].lower() + roll[-3:] + "@mietjammu.in"

print("Email:", email)