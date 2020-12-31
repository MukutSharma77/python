'''
Write a function that takes a two-digit number and determines if it's the largest of two possible digit swaps.
To illustrate:
largest_swap(27) ➞ False
largest_swap(43) ➞ True
If 27 is our input, we should return False because swapping the digits gives us 72, and 72 > 27. On the other hand, swapping 43 gives us 34, and 43 > 34.

'''

def function(num):
    num=str(num)
    if int(num) > int(num[::-1]):
        print(True)
    else:
        print(False)


num=int(input("Enter Number :   "))
function(num)