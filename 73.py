#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area

#Class name Rectangle function area is used to to find area of rectangle

class Rectangle:

    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        print("The area of rectangle is :   ",self.l * self.w)

#input length and width from user

l=float(input("Enter Length of a recatngle  :   "))
w=float(input("Enter Width of a recatngle  :    "))

obj=Rectangle(l,w)
obj.area()