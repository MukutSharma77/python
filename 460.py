'''Give Me the Even Numbers
Create a function that takes two parameters (start, stop), and returns the sum of all even numbers in the range.
Examples
sum_even_nums_in_range(10, 20) ➞ 90
# 10, 12, 14, 16, 18, 20
sum_even_nums_in_range(51, 150) ➞ 5050
sum_even_nums_in_range(63, 97) ➞ 1360'''

to_=51
from_=150
tot=0
for i in range(to_,from_+1):
    if i % 2==0:
        tot+=i
print(tot)