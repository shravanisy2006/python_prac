fact=[]
sum=0
n=int(input("Enter a number:"))
for i in range (1,n):
    if n%i==0:
        fact.append(i)
for facts in fact:
    sum+=facts
if sum==n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
