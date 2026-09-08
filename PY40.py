# WAP to create a simple password validation system. The program should repeatedly ask the user to enter a password until the valid password is entered.
# A password will be considered valid if it has at least 8 characters and contains the @ symbol.
# Once the user enters a valid password, the program should display "Password accepted" and stop. Other wise it should display "Weak Password. Try again"
# and ask for the password again.

while True:
    password = input("Enter password: ")

    if len(password) >= 8 and "@" in password:
        print("Password accepted")
        break
    else:
        print("Weak Password. Try again")

