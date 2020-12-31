'''
Divides Evenly
Given two integers, a and b, return True if a can be divided evenly by b. Return False otherwise.
Examples
divides_evenly(98, 7) ➞ True
# 98/7 = 14
divides_evenly(85, 4) ➞ False
# 85/4 = 21.25
'''



num1=int(input("Enter Number:  "))
num2=int(input("Enter Number:  "))

if num1 % num2 == 0:
    print(True)
else:
    print(False)