''' Add the following two NumPy arrays and Modify a result array by calculating the square of each element
import numpy
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
Expected Output:
addition of two arrays is
[[20 39 33]
 [25 25 28]]
Result array after calculating the square root of all elements
[[ 400 1521 1089]
 [ 625  625  784]]'''


import numpy
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

tot=arrayOne+arrayTwo
print("addition of two array is :   \n",tot)

sq=tot**2
print("Square of total array :  \n",sq)