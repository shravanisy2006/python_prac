n=int(input("Enter any number: "))
sum1=0
sum2=0
for i in range (1,n+1):
    if i%2 == 0:
        sum1+=i
    else:
        sum2+=i
print(f"Your even and odd sum are {sum1} and {sum2} respectively.") 
