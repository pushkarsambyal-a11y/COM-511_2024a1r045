# Write a Python program that asks the user to enter a username and password. The user should get only 3 attempts. 
# If the correct credentials are entered, display "Login Successful" and stop the loop. If all attempts are used, display "Account Locked"

username = "admin"
password = "password123"
attempts = 3

while attempts > 0:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_username == username and entered_password == password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print(f"Incorrect credentials. You have {attempts} attempts left.")

if attempts == 0:
    print("Account Locked")
    