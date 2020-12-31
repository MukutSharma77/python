'''Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.'''

#inputting age and name from user
name=input("Enter Your Name :    ")
age=int(input("Enter your age  :   "))

#checking is user is less than 100 of age Calculating and printinting when will be 100 yr old (100-age)

if age <= 100:
    print(f"Hey {name.title()} \nAfter {100 - age} Years you will be 100 yr old")
else:
    print("You are already above 100")