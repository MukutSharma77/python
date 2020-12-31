'''Say "Hello" Say "Bye"
Write a function that takes a string name and a number num (either 0 or 1) and return "Hello" + name if num is 1, otherwise return "Bye" + name.
Examples
say_hello_bye("alon", 1) ➞ "Hello Alon"
say_hello_bye("Tomi", 0) ➞ "Bye Tomi"
say_hello_bye("jose", 0) ➞ "Bye Jose"'''

no=input("Enter Number (0 or 1)  :  ")
no=int(no)
name=input("ENetr Yoyur name :  ")
if no==0:
    print(f"Bye {name}")
elif no==1:
    print(f"Hi {name}")
else:
    print("Invalid")