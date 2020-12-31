'''
Sum of the Odd Numbers
Create a function which returns the total of all odd numbers up to and including n. n will be given as an odd number.
Examples
add_odd_to_n(5) ➞ 9
# 1 + 3 + 5 = 9
'''

num=int(input("Enter Number :  "))
tot=0
for i in range(1,num+1,2):
    tot+=i

print(tot)