'''Recursion: Factorials
Write a function that calculates the factorial of a number recursively.
Examples
factorial(5) ➞ 120
factorial(3) ➞ 6
factorial(1) ➞ 1
factorial(0) ➞ 1'''

def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num * factorial(num-1)

num=5
output=factorial(num)
print(output)