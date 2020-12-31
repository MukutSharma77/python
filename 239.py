#Write a Python program to check if two given numbers are coprime or not. Return True if two numbers are coprime otherwise return false.

num1=int(input("Enter Numhber 1 :   "))
num2=int(input("Enter Numhber 2 :   "))

list1=[]
for i in range(1,num1+1):
    if num1 % i==0:
        list1.append(i)

list2 = []
for i in range(1, num2 + 1):
    if num2 % i == 0:
        list2.append(i)

list1=set(list1)
list2=set(list2)

z=list1.intersection(list2)


if len(z)==1:
    print("Co prime number")
else:
    print("Not a co prime number")