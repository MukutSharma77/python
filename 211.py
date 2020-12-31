#Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

#Inputting number
num1=int(input("Enter Number1 :   "))
num2=int(input("Enter Number2 :   "))

if num1==num2:
    print("Both numbers are equal")
    print("Three times of sum :   ",3*(num2+num1))
else:
    print("the sum of two number is :  ",num1+num2)