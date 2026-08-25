n = int(input("Enter the amount: "))

temp = n//500

remain = n % 500

temp2 = remain//100

print(f"You need '{temp}' 500 notes and '{temp2}' 100 notes")