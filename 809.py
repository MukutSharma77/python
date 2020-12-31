'''Count Number of Instances
Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be accessed as a class attribute.
Examples
u1 = User("johnsmith10")
User.user_count ➞ 1
u2 = User("marysue1989")
User.user_count ➞ 2
u3 = User("milan_rodrick")
User.user_count ➞ 3'''

class User:
    lst=[]
    def __init__(self,string):
        self.string=string
        User.lst.append(self.string)
        print(len(User.lst))

    def user_count(self):

        User.lst.append(self.string)
        print(len(User.lst))


u1 = User("johnsmith10")
User.user_count
u2 = User("marysue1989")
User.user_count
u3 = User("milan_rodrick")
User.user_count