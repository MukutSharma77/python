'''Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example,
Given input array A = [1,1,2],'''

from array import *

arr=array('i',[1,1,2])

arr=sorted(arr)
arr=list(set(arr))

print("array is :  ",arr)
print("Lemngth :  ",len(arr))