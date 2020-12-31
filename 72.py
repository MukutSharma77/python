#Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.


#claass of name circle in it function name formula in  it we have formula takling radius from user

class Circle:

    def __init__(self,radius):
        self.radius=radius

    def formula(self):
        area=3.14 * self.radius ** 2
        print("The area is : ",area.__round__(2))


#CALLING CLASS 
radius=float(input("Enter Radius :   "))
obj=Circle(radius)
obj.formula()
