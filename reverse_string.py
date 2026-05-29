#To reverse the string

a=input("Please enter a string: ")
b=""
for char in range(len(a)-1,-1,-1):
    b+=a[char]
print(b)
