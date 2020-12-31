'''Equality of 3 Values
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2
equal(1, 1, 1) ➞ 3
equal(3, 4, 1) ➞ 0
Notes
Your function must return 0, 2 or 3.
'''

tup_=(3,4,1)

if len(tup_) == tup_.count(tup_[0]):
    print(3)

elif tup_[0]==tup_[2] or tup_[0]==tup_[1] or tup_[1]==tup_[2]:
    print(2)

else:
    print(0)