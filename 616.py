'''Write a function that mimics (without the use of <<) the left shift operator and returns the result from the two given integers.
Examples
shift_to_left(5, 2) ➞ 20
shift_to_left(10, 3) ➞ 80
shift_to_left(-32, 2) ➞ -128
shift_to_left(-6, 5) ➞ -192
shift_to_left(12, 4) ➞ 192
shift_to_left(46, 6) ➞ 2944
FORMULA=x*2**y'''

num1=10
num2=3
print(num1*2**num2)