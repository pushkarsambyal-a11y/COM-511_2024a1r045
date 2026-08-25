sub1 = int(input("Marks of 1st subject: "))
sub2 = int(input("Marks of 2nd subject: "))
sub3 = int(input("Marks of 3rd subject: "))

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and (sub1 + sub2 + sub3)/3 >= 50:
    print("True")
else:
    print("False")
