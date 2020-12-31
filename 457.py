'''How Many Decimal Places?
Create a function that returns the number of decimal places a number has. Any zeros after the decimal point count towards the number of decimal places.
Examples
get_decimal_places("43.20") ➞ 2
get_decimal_places("400") ➞ 0
get_decimal_places("3.1") ➞ 1'''

num=43.20
num=str(num)
if '.' in num:
    num=str(num).split('.')
    print(num[1])
else:
    print('0')