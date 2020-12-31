# Write a Python program to test whether a number is within 100 of 1000 or 2000

num=int(input("Enter Number :   "))

if num <= 100:
    print("Inputted number is within 100")

elif num <= 1000:
    print("Number is within 1000")

elif num<=2000:
    print("Number is within 2000")
else:
    print("Number is greater than 2000")