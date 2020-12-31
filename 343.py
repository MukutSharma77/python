'''A bartender is writing a simple program to determine whether he should serve drinks to someone. He only serves drinks to people 18 and older and when he's not on break.
Given the person's age, and whether break time is in session, create a function which returns whether he should serve drinks.
Examples
should_serve_drinks(17, True) ➞ False
should_serve_drinks(19, False) ➞ True
should_serve_drinks(30, True) ➞ False
'''
def should_serve_drinks(age,brk):
    if age >= 18 and brk=='false':
        print(True)
    else:
        print(False)


age=int(input("Enter age  :   "))
brk=input(("Break (True or False)  :  ")).lower()
should_serve_drinks(age,brk)