fact=[]
n=int(input("Enter any number:"))
for i in range (1,n+1):
    if n%i==0:
        fact.append(i)
num=len(fact)
if num==2:
    print(f"{n} is Prime Number.")
else:
    print(f"{n} is not a Prime Number.")
