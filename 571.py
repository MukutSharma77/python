'''Recursion: Fibonacci Numbers
Fibonacci numbers are created in the following way:
F(0) = 0
F(1) = 1
..
F(n) = F(n-2) + F(n-1)
Write a function that calculates the nth Fibonacci number.
Examples
fib(0) ➞ 0
fib(1) ➞ 1
fib(2) ➞ 1
fib(8) ➞ 21
'''

def fib(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fib(num-2) +fib(num-1)

num=8
output=fib(num)
print(output)