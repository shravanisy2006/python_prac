a = int(input("Enter a number:"))

num= a
rev = 0
while a > 0:
    rev = rev * 10 + a % 10
    a= a// 10
if num == rev:
    print(f"{num} is a Palindromic Number.")
else:
    print(f"{num} is not a Palindromic Number")
