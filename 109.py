#Python Program to Create a Class which Performs Basic Calculator Operations

#class  name calulator consist function name add , sub , mul used to add , subtract , multiplication
class Calculator:
    def __init__(self):
        self.num1=0
        self.num2 = 0
        self.tot=0

    def add(self):
        self.num1=int(input("Enter Number 1  :   "))
        self.num2=int(input("Enter Number 2  :   "))
        self.tot=self.num1+self.num2
        print("The total of two number is :    ",self.tot)

    def sub(self):
        self.num1=int(input("Enter Number 1  :   "))
        self.num2=int(input("Enter Number 2  :   "))
        self.tot=self.num1-self.num2
        print("The Subtraction of two number is :    ",self.tot)

    def mul(self):
        self.num1=int(input("Enter Number 1  :   "))
        self.num2=int(input("Enter Number 2  :   "))
        self.tot=self.num1*self.num2
        print("The Multiplication of two number is :    ",self.tot)



#calling Class and their functiopn
obj=Calculator()
obj.add()
obj.sub()
obj.mul()