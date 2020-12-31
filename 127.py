'''Create a function that takes a list of numbers
and return its median. If the input list is even length, take the average of the two medians, else, take the single median.'''

import math
# list_= [3, 13, 7, 5, 21, 23, 39, 23, 40, 23, 14, 12, 56, 23, 29]
list_= [3, 5, 7, 12, 13, 14, 21, 23, 23, 23, 23, 29, 40, 56]

#If list is even than taking avergrage of two number
if len(list_) % 2 == 0:
    val = len(list_) // 2
    list_.sort()
    print("The median from list is :   ", (list_[val] + list_[val-1])/2)

#if list is odd printing cetener index
else:
    val=len(list_)//2
    list_.sort()
    print("The median from list is :   ",list_[val])