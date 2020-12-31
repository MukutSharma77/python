'''Length of Number
Create a function that takes a number num and returns its length.
Examples
number_length(10) ➞ 2
number_length(5000) ➞ 4
number_length(0) ➞ 1
Notes
DO NOT USE LEN() FOR THIS CHALLENGE
'''

num=0
count=0

if num>0:
    while num:
        count+=1
        num//=10

    print(count)
else:
    print(1)