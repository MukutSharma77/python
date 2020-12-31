'''Python Program to remove duplicate value from array'''

from array import *

arr=array('i',[1,2,3,4,5 , 1, 2 ,3 ,4 ,5 ,5 ,6 ,6 ,7 ,7 ])
arr_output=array('i',[])
tot=1
for i in arr:
    if i not in arr_output:
        arr_output.append(i)
print(arr_output)