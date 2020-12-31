'''Make a Circle with OOP
Your task is to create a Circle constructor that creates a circle with a radius provided by an argument. The circles constructed must have two getters getArea() (PIr^2) and getPerimeter() (2PI*r) which give both respective areas and perimeter (circumference).
For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
Examples
circy = Circle(11)
circy.getArea()
# Should return 380.132711084365
circy = Circle(4.44)
circy.getPerimeter()
# Should return 27.897342763877365
Notes
Round results up to the nearest integer.'''


class Circle:
    def __init__(self,r):
        self.r=r

    def getPerimeter(self):
        return 2 * 3.141 * self.r

    def getArea(self):
        return 3.141 * self.r * self.r

obj=Circle(11)
output=obj.getArea()
print(output)
output=obj.getPerimeter()
print(output)