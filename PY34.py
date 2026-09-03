# Take an email address and print username, domain, and reversed domain.
email = input("Enter email address: ")

username = email.split("@")[0]
domain = email.split("@")[1]
reverse = domain[::-1]

print("Username:", username)
print("Domain:", domain)
print("Reversed Domain:", reverse) 