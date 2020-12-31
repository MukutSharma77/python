'''Summing a Slice
Given a list and an integer n, return the sum of the first n numbers in the list.
Worked Example
sum_first_n_nums([9, 8, 7, 6], 3) ➞ 24
# The parameter n is specified as 3.
'''

list_=[9, 8, 7, 6]

num=int(input("Enter Number :  "))
if len(list_) >= num:
    tot=0
    for i in list_[:num]:
        tot+=i
    print(tot)

else:
    print("Invalid input")