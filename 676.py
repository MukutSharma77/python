'''Convert a Number to Base-2
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Examples
binary(1) ➞ "1"
binary(5) ➞ "101"
binary(10) ➞ "1010"'''

num=5
bin_=bin(num)
print(str(bin_[2:]))