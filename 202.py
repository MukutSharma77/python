#Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

name=input("Enter Name :    ").title()
last_name=input("Enter Last name :   ").title()

full_name=last_name+"  "+name

print("Hello ",full_name)