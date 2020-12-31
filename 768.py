'''Iterated Square Root
The iterated square root of a number is the number of times the square root function must be applied to bring the number strictly under 2.
Given an integer, return its iterated square root. Return "invalid" if it is negative.
Examples
i_sqrt(1) ➞ 0
i_sqrt(2) ➞ 1
i_sqrt(7) ➞ 2
i_sqrt(27) ➞ 3
i_sqrt(256) ➞ 4
i_sqrt(-1) ➞ "invalid"'''

num=256

if num==1:
    print(0)

elif num==2:
    print(1)

elif num>2:
    count=0
    i=2
    import math
    while num>=2:
        num=math.sqrt(num)
        count+=1
    print(count)

else:
    print('invalid')