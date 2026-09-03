# Take a password and check length, presence of @, and whether first and last characters are different.
password = input("Enter password: ")

print("Length:", len(password))
print("Contains @:", "@" in password)
print("First and last characters are different:", password[0] != password[-1])