'''Is This a Right Angled Triangle?
Given three numbers, x, y and z, determine whether they are the edges of a right angled triangle.
Examples
right_triangle(3, 4, 5) ➞ True
# This is the classic example of a "nice" right angled triangle.
right_triangle(145, 105, 100) ➞ True
# This is a less famous example.
right_triangle(70, 130, 110) ➞ False
# This isn't a right angled triangle.
(x*x + y*y + z*z) - max(x,y,z)**2 == max(x,y,z)**2

'''

x=3
y=4
z=5

print((x**2 + y**2 + z**2) - max(x,y,z)**2==max(x,y,z)**2)