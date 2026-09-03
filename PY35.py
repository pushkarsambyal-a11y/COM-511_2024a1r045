# Take name, branch, and year. Generate a code name using string concatenation, slicing, and repetition.

name = input("Enter name: ")
branch = input("Enter branch: ")
year = input("Enter year: ")

code = name[:3].upper() + branch[:3].upper() + year[-1] * 2

print("Code Name:", code)