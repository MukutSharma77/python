'''Highest Digit
Create a function that takes a number as an argument and returns the highest digit in that number.
Examples
highest_digit(379) ➞ 9
highest_digit(2) ➞ 2
highest_digit(377401) ➞ 7'''

num=379
num=str(num)

list_=[]
for i in num:
    list_.append(str(i))

print(max(list_))