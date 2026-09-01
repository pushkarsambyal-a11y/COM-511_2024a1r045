# Write a Pyhton program to take a students full name and display:
# Total no of character 
# First Character
# Last character
# Name in uppercase form.

Name = input("Enter the name : ")

print("Total characters : ",len(Name))
print("First character : ",Name[0])
print("Last character : ",Name[-1])
print("Capitalized : ",Name.upper())

