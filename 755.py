'''Name Classes
Write a class called Name and create the following attributes given a first name and last name (as fname and lname):
An attribute called fullname which returns the first and last names.
A attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.
Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"
a1.lname ➞ "Smith"
a1.fullname ➞ "John Smith"
a1.initials ➞ "J.S"
Notes
Make sure only the first letter of each name is capitalised.
Check the Resources tab for some helpful tutorials on Python classes.
756)'''

class Name:
    def __init__(self,f_name,l_name):
        self.f_name=f_name
        self.l_name = l_name
    def fname(self):
        print(self.f_name)
    def lname(self):
        print(self.l_name)
    def fullname(self):
        print(self.f_name+' '+self.l_name)


a1 = Name("john".title(), "SMITH".title())
a1.fname()
a1.lname()
a1.fullname()