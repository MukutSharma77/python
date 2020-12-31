'''Sum of Evenly Divisible Numbers from a Range
Create a function that takes three arguments a, b, c and returns the sum of the numbers that are evenly divided by c from the range a, b inclusive.
Examples
evenly_divisible(1, 10, 20) ➞ 0
# No number between 1 and 10 can be evenly divided by 20.
evenly_divisible(1, 10, 2) ➞ 30
# 2 + 4 + 6 + 8 + 10 = 30
evenly_divisible(1, 10, 3) ➞ 18
# 3 + 6 + 9 = 18
'''

num=input("Enter Number comma seprated :  ").split(',')
tot=0

for i in range(len(num)):
    num[i]=int(num[i])
print(num)
for i in range(0 , num[1]+1 , num[2]):
    tot+=int(i)
    # print(i)

print(tot)