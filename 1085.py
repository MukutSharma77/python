'''Create a 4X2 integer array and Prints its attributes
[64392 , 31655 , 32579  ,   0 ,49248 ,  462 , 0  ,    0]
Note: The element must be a type of unsigned int16. And print the following Attributes: –
The shape of an array.
Array dimensions.
The Length of each element of the array in bytes.

Expected Output:
Printing Array
[[64392 31655]
 [32579     0]
 [49248   462]
 [    0     0]]

Printing NumPy array Attributes

1> Array Shape is:  (4, 2)
2>. Array dimensions are  2
3>. Length of each element of array in bytes is  8'''


from numpy import *

def arr(array_):
    array_2D=array_.reshape(4,2)
    print("2-D Array is :   ")
    print(array_2D)
    print('\n> Array shape is : ',array_2D.shape)
    print('> Array dimension are : ', array_2D.ndim)
    print('> Length of each element of array in bytes is ', array_2D.itemsize)



array_=array([64392 , 31655 , 32579  ,   0 ,49248 ,  462 , 0  ,    0])
arr(array_)
