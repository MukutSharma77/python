'''Number of Squares in an N * N Grid
Create a function that calculates the number of different squares in an n * n square grid. Check the Resources tab.
Examples
number_squares(2) ➞ 5
number_squares(4) ➞ 30
number_squares(5) ➞ 55
Notes
Input is a positive integer.
Square pyramidal number.'''

num=5
tot=0

for i in range(1,num+1):
    tot+=i**2

print(tot)