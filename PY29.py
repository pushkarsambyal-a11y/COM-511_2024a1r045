# WAP to take a string and seperate characters present at even index positions and odd index positions

s = input("Enter a string: ") 
even = s[::2] 
odd = s[1::2] 
print("Characters at even index positions:", even) 
print("Characters at odd index positions:", odd)