#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero

num1=int(input("Enter number 1  :   "))
num2=int(input("Enter number 2  :   "))
num3=int(input("Enter number 3  :   "))


if num1 == num3 and num1==num2:
    print("Sum is :   ",num3+num1+num2)

elif num1 == num3 and num3==num1:
    print("Sum is :   0")


elif num2 == num3 and num3==num2:
    print("Sum is :   0")


elif num1 == num2 and num2==num1:
    print("Sum is :   0")

else:
    print("Sum is   :  ",sum(num1,num2,num3))