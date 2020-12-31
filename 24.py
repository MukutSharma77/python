#Define class two methd one for getting string and seconf for printing string

class ques:

    def get_string(self):
        self.name=input("Enter name  :     ")
        self.last_name=input("Enter Last Name  :     ")

    def printstr(self):
        print("My name is :   "+self.name + " " +self.last_name)

obj=ques()
obj.get_string()
obj.printstr()