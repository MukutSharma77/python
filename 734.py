'''Reversing a Binary String
Write a function that takes an integer n, reverses the binary representation of that integer, and returns the new integer from the reversed binary.
Examples
reversed_binary_integer(10) ➞ 5
# 10 = 1010 -> 0101 = 5
reversed_binary_integer(12) ➞ 3
# 12 = 1100 -> 0011 = 3
reversed_binary_integer(25) ➞ 19
# 25 = 11001 -> 10011 = 19
reversed_binary_integer(45) ➞ 45
# 45 = 101101 -> 101101 = 45
'''

num=45
bin_=bin(num)
rev=bin_
rev=rev[2:]
lst=[int(rev[i])*2**i for i in range(len(str(rev)))]
print(sum(lst))