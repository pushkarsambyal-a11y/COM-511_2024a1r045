balance = int(input("Enter the balance: "))

dep = int(input("Enter money to deposit: "))
balance += dep
print(f"Balance after deposit = {balance}")

wid = int(input("Enter money to withdraw: "))
balance -= wid
print(f"Balance after withdraw = {balance}")

mul = int(input("Enter the operand: "))
balance *= mul
print(f"Balance after multiplying = {balance}")

div = int(input("Enter the operand: "))
balance /= div

print(f"The final balance = {balance}")