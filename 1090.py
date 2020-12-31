'''Split the array into four equal-sized sub-arrays
Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
Expected Output:
Creating 8X3 array using numpy.arange
[[10 11 12]
 [13 14 15]
 [16 17 18]
 [19 20 21]
 [22 23 24]
 [25 26 27]
 [28 29 30]
 [31 32 33]]
Dividing 8X3 array into 4 sub array
[array([[10, 11, 12],[13, 14, 15]]),
array([[16, 17, 18],[19, 20, 21]]),
array([[22, 23, 24],[25, 26, 27]]),
array([[28, 29, 30],[31, 32, 33]])]'''

import numpy

arr_=numpy.arange(10,34,1)
arr_=arr_.reshape(8,3)
print('Creating 8X3 array using numpy.arange  :   ')
print(arr_)

arr_split=numpy.split(arr_,4)
print('Spliting array :  ')
print(arr_split)