'''Binary to Decimal Converter
You are given one input: A list containing eight 1's and/or 0's. Write a function that takes an 8 bit binary number and convert it to decimal.
Examples
binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1]) ➞ 255
binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0]) ➞ 0
binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0]) ➞ 188'''

def binary_to_decimal(lst):
    if len(lst)==8:
        tot=0
        lst.reverse()
        for i in range(1,len(lst)):
            tot+=lst[i] * 2**i
    print(tot)

binary_to_decimal([1, 1, 1, 1, 1, 1, 1, 1])
binary_to_decimal([0, 0, 0, 0, 0, 0, 0, 0])
binary_to_decimal([1, 0, 1, 1, 1, 1, 0, 0])