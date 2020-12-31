'''Create a method in the Person class which returns how another person's age compares. Given the objects p1, p2 and p3, which will be initialised with the attributes name and age, return a sentence in the following format:
{other_person} is {older than / younger than / the same age as} me.
Examples
p1 = Person("Samuel", 24)
p2 = Person("Joel", 36)
'''

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def comapre_age(self):
        if self.age > 20:
            print(f"{self.name} is Older than me")
        elif self.age < 20:
            print(f"{self.name} is Younger than me")
        else:
            print(f"{self.name} is same age")

p1 = Person("Samuel", 24)
p2 = Person("Joel", 11)
p1.comapre_age()
p2.comapre_age()