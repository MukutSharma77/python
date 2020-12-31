'''Limit a Number's Value
Create a function that takes three number arguments — one number as an input and two additional numbers representing the endpoints of a closed range — and return the number limited to this range.
If the number falls within the range, the number should be returned.
If the number is less than the lower limit of the range, the lower limit should be returned.
If the number is greater than the upper limit of the range, the upper limit should be returned.
Examples
limit_number(5, 1, 10) ➞ 5
limit_number(-3, 1, 10) ➞ 1
limit_number(14, 1, 10) ➞ 10
limit_number(4.6, 1, 10) ➞ 4.6
'''

num1=float(input('Enter Number 1 :  '))
num2=float(input('Enter Number 2 :  '))
num3=float(input('Enter Number 3 :  '))
list_=[num1,num2,num3]
list_.sort()
print(list_[1])