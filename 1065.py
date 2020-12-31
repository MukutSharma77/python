'''Python Program to multiplication of array'''

from array import *

arr=array('i',[1,2,3,4,5])

tot=1
for i in arr:
    tot*=i
print(tot)