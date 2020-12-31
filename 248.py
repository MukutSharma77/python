#Python Program to Check if a Number is a Strong Number

num=int(input("Enter Number :   "))

fact=1
tot=0
for no in str(num):
    no=int(no)
    fact=1
    for i in range(1,no+1):
        fact*=i
    tot+=fact


if num==tot:
    print("Yes number is strong number")
else:
    print("Not a strong number")