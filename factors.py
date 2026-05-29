fact=[]
n=int(input("Enter a number:"))
for i in range (1,n+1):
    if n%i==0:
        fact.append(i)
print(f"The factors of {n} are: {fact}")
