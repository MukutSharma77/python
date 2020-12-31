'''Given the radius of a circle and the area of a square, return True if the circumference of the cirlce is greater than the square's perimeter and False
if the square's perimeter is greater then the circumference of the circle.'''


#Inputtimg Radius of Circle  and side of a square

radius = float(input("Enter Radius of a Cicle :   " ))

side = float(input("Enter Side of a Square  :   " ))


# Checking if circumference of a circe is greater than perimeter of square than True else false
if (3.14 * radius * radius) > (4*side):
    print(True)
elif (3.14 * radius * radius) < (4*side):
    print(False)
else:
    print("Both are equal")