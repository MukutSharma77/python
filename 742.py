'''Power of Two
Write a function that returns True if an integer can be expressed as a power of base value 2 and False otherwise.
Examples
power_of_two(32) ➞ True
power_of_two(1) ➞ True
power_of_two(18) ➞ False'''

num=18

two=0
count=0
for i in range(0,num):
    two=2**i

    if two==num:
        count+=1
        break

print(count>0)