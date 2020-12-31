#Write a Python program to input a number, if it is not a number generate an error message.

num=input("Enter a number :  ")
if num.isdigit():
    print("Number is :   ",num)
else:
    print("Please enter a number")