# Write a pyhton program to calculate the final bill amount after applying a discount. The program should take the total bill anmount as input from the
# user and apply the discount according to the follwoing rules. After calculating the discount amount and the final bill amount payable by the customer.

bill = float(input("Enter bill amount : "))

if bill > 5000:
    discount = bill * 20 / 100
elif bill >= 3000:
    discount = bill * 10 / 100
else:
    discount = 0

final_bill = bill - discount

print("Discount Amount : ",discount)
print("Final Bill Amount : ",final_bill)