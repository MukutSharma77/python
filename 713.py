'''The Fibonacci Number
Create a function that, given a number, returns the corresponding value of that index in the Fibonacci series.
Examples
fibonacci(3) ➞ 3
fibonacci(7) ➞ 21
fibonacci(12) ➞ 233'''

def fibonacci(num):
    count=1
    a=0
    b=1
    while count<=num:
        c=a+b

        a,b=b,c
        count+=1

    print(c)

num=12
fibonacci(num)