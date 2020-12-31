'''Round to Closest N
Create a function that takes two integers, num and n, and returns an integer which is divisible by n and is the closest to num. If there are two numbers equidistant from num and divisible by n, select the larger one.
Examples
round_number(33, 25) ➞ 25
round_number(46, 7) ➞ 49
round_number(133, 14) ➞ 140'''

def round_number(num,n):
    d=num%n
    u=-num % n
    if d<u:
        print(num-d)
    else:
        print(num+u)

round_number(33, 25)
round_number(46, 7)
round_number(133, 14)