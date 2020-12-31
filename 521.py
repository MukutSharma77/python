'''The Collatz Conjecture
Create a function, example:
10 is number
10 is even - 10 / 2 = 5
5 is odd - 5 * 3 + 1 = 16
16 is even - 16 / 2 = 8
8 is even - 8 / 2 = 4
4 is even - 4 / 2 = 2
2 is even - 2 / 2 = 1 -> if reach 1, return 6 steps
Consider the following operation on an arbitrary positive integer:
if n is even -> n / 2
if n is odd -> n * 3 + 1'''

num=8


if num%2==0:
    print(num//2)
else:
    print(num*3+1)