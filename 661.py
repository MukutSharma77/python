'''Even or Odd Number of Factors
Create a function that returns "even" if a number has an even number of factors and "odd" if a number has an odd number of factors.
Examples
factor_group(33) ➞ "even"
factor_group(36) ➞ "odd"
factor_group(7) ➞ "even"
'''

num=7
count=0
for i in range(1,num+1):
    if num % i ==0:
        count+=1

if count%2==0:
    print('Even')
else:
    print('Odd')