'''Write a function that finds the sum of the first n natural numbers. Make your function recursive.
Examples
sum_numbers(5) ➞ 15
# 1 + 2 + 3 + 4 + 5 = 15
sum_numbers(1) ➞ 1
sum_numbers(12) ➞ 78'''

num=12
if  num>1:
    tot=0
    for i in range(num+1):
        tot+=i

print(tot)