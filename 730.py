'''Simple Circle Collision Detection
Create a function that returns True if the given circles are intersecting, otherwise return False. The circles are given as two lists containing the values in the following order:
Radius of the circle.
Center position on the x-axis.
Center position on the y-axis.
Examples
is_circle_collision([10, 0, 0], [10, 10, 10]) ➞ True
is_circle_collision([1, 0, 0], [1, 10, 10]) ➞ False
Notes
 C1C2 = sqrt((x1 - x2)2 + (y1 - y2)2).
 If C1C2 < R1 + R2
      Circle intersects each other.'''

import math

cir1=[1, 0, 0]
cir2= [1, 10, 10]

radius=cir1[0]+cir2[0]
xy=math.sqrt ((cir1[1] - cir2[1])**2 + (cir1[2] - cir2[2])**2)
print(radius > xy)