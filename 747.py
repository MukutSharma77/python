'''Pandigital Numbers
A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, returning True if the integer is pandigital, and False otherwise.
Examples
is_pandigital(98140723568910) ➞ True
is_pandigital(90864523148909) ➞ False
# 7 is missing.
is_pandigital(112233445566778899) ➞ False'''

num=98140723568910
lst=[i for i in range(0,10)]
print(lst)

lst_num=[]
for i in str(num):
    lst_num.append(int(i))

print(list(set(lst_num))==lst)