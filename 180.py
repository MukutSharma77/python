#Calculate the hypotenuse of a right angled triangle

#imposting math
import math

# inputing  b p
b=float(input("Enter Base   :     "))
p=float(input("ENter parpandicular   :    "))

# formula h = sqrt(p^2 + b^2)
h= math.sqrt((b**2) + (p**2))

print("The hypotenuse is :   ",h)