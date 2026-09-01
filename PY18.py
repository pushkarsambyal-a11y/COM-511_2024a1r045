# Write a Pyhton program to take a student name and roll no, then generate a username using the first 3 letters of the name and last 2 digits of the roll no.

name = input("Enter the name : ")
roll = input("Enter roll no : ")


username = name[:3] + roll[-2:]

print("Username : ",username)