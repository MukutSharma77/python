'''Evaluating Factorials
Create a function that takes a list of factorial expressions and returns the sum.
Examples
eval_factorial(["2!", "3!"]) ➞ 8
eval_factorial(["5!", "4!", "2!"]) ➞ 146
eval_factorial(["0!", "1!"]) ➞ 2
Notes
0! and 1! both equal 1.'''

lst=[ "1!", "0!"]
tot=0
for i in lst:
    i=int(i.replace('!',''))
    # print(i)
    fact=1
    for j in range(1,i+1):
        fact*=j
    tot+=fact

print(tot)