'''Next Number Greater Than A and B and Divisible by B
You are given two numbers a and b. Create a function that returns the next number greater than a and b and divisible by b.
Examples
divisible_by_b(17, 8) ➞ 24
divisible_by_b(98, 3) ➞ 99
divisible_by_b(14, 11) ➞ 22'''

def divisible_by_b(a,b):
    i=a+1
    while True:
        if i % b == 0:
            print(i)
            break
        i+=1

divisible_by_b(17, 8)
divisible_by_b(98, 3)
divisible_by_b(14, 11)
