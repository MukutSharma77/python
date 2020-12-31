'''Negate the List of Numbers
Given a list of numbers, negate all elements contained within.
Negating a positive value -+n will return -n, because all +'s are removed.
Negating a negative value --n will return n, because the first - turns the second minus into a +.
Examples
negate([1, 2, 3, 4]) ➞ [-1, -2, -3, -4]
negate([-1, 2, -3, 4]) ➞ [1, -2, 3, -4]'''


list_=[-1, 2, -3, 4]
list_2=[]
for i in list_:
    list_2.append(i*-1)

print(list_2)