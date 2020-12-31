'''Find the Total Number of Digits the Given Number Has
Create a function that takes a number as an argument and returns the amount of digits it has.
Examples
find_digit_amount(123) ➞ 3
find_digit_amount(56) ➞ 2
find_digit_amount(7154) ➞ 4
find_digit_amount(61217311514) ➞ 11
find_digit_amount(0) ➞ 1
'''

num=61217311514

count=0
while num:
    count+=1
    num=num//10

print(count)