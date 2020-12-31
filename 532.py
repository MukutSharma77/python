'''Square Every Digit
Create a function that squares every digit of a number.
Examples
square_digits(9119) ➞ 811181
square_digits(2483) ➞ 416649
square_digits(3212) ➞ 9414'''

num=2483

for i in str(num):
    i=int(i)
    print(i**2,end="")