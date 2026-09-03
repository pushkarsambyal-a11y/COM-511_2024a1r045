# Take roll number like 2024A1R057 and extract admission year, program code, and roll number digits using slicing.


roll = input("Enter roll number: ")

year = roll[:4]
program = roll[4:7]
number = roll[7:]

print("Admission Year:", year)
print("Program Code:", program)
print("Roll Number:", number)