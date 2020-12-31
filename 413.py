'''Product Divisible by Sum?
Write a function that returns True if the product of a list is divisible by the sum of that same list. Otherwise, return False.
Examples
divisible([3, 2, 4, 2]) ➞ False
divisible([4, 2, 6]) ➞ True
# 4 * 2 * 6 / 4 + 2 + 6
divisible([3, 5, 1]) ➞ False'''

list1=[4,2,6]

product=1
for i in list1:
    product*=i


if product % sum(list1)==0:
    print(True)
else:
    print(False)