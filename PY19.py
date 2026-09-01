# WAP to take an email address and print the domain name.

email = input("Enter email : ")

domain = email.split("@")[1]

print("Domain : ", domain)