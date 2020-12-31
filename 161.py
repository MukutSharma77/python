#Python program to find perfect number


#Inputing Number

num=int(input("Enter Number :    "))


#Checking is it perfect number
tot=0
for i in range(1,num):
    if num % i ==0:
        tot+=i

if num==tot:
    print("Yes it is Perfect number ")
else:
    print("Not a perfect number")