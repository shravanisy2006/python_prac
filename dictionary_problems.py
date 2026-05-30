# Write a Python script to merge two Python dictionaries?

d1={10:100,20:200,30:300}
d2={40:400,50:500,60:600}

for i in d2:
    d1[i] = d2[i]
print(d1)

# Write a Python program to sum all the values in a dictionary?

d1={10:100,20:200,30:300}
sum=0
for i in d1:
    a=(d1[i])
    sum+=a
print(f"The sum of the values in d1 is: {sum}")

# Count the frequency of each element

a=[1,2,4,6,1,4,2,7,4,8,4,2]
d={}
for i in a:
  if i in d.keys():
    d[i]+=1
  else:
    d[i]=1
print(d)
