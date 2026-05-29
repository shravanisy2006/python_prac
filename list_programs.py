# Print positive and negative elements of an List?

a=[4 , -2 , 23 , 56 , 74 , -5 , -7 , -9 , 14]
negative_num=[]
positive_num=[]
for i in a:
    if (i<0):
        negative_num.append(i)
    else:
         positive_num.append(i)
print("Positive Numbers: ",positive_num)
print("Negative Numbers: ",negative_num)

#Mean of List elements?

a=[4 , 23 , 56 , 74 , 14]
sum=0
for i in a:
    sum+=i
    n=len(a)
    Mean=sum/n
print(f"The mean of the elements in the list is: {Mean}")

#Find the greatest element and print its index too?

a=[4 , 23 , 56 , 74 , 14]
largest=a[0]
index=0
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
print(f"The largest number is {largest} at index number {index}.")


