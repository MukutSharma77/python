#Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user

num1=int(input("Enter Number 1 :   "))
num2=int(input("Enter Number 2 :   "))

if num1 % num2 ==0:
    print("True")
else:
    print(False)