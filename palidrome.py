a=input("Please enter a string: ")
b=""
for char in range(len(a)-1,-1,-1):
    b+=a[char]
if a==b:
    print("The string is a palidrome.")
else:
    print("The string is not a palidrome.")
    
