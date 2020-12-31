'''Sum of Every Nth Number
Given a list of numbers and a positive value for n, return the sum of every nth number in the list.
Examples
sum_every_nth([4, 8, 6, 6, 7, 9, 3], 1) ➞ 43
# 4+8+6+6+7+9+3 = 43
sum_every_nth([7, 3, 10, 4, 5, 8, 4, 9, 6, 9, 10, 1, 4], 4) ➞ 14
# 4+9+1 = 14
sum_every_nth([10, 6, 5, 4, 5, 2, 3, 3, 8, 10, 7, 2], 8) ➞ 3
# 3
sum_every_nth([6, 8, 9, 4, 6, 4, 7, 1, 5, 6, 10, 2], 13) ➞ 0
# only 12 numbers in list'''
lst=[4, 8, 6, 6, 7, 9, 3]
num=1

tot=0
for i in range(num-1,len(lst),num):

    tot+=lst[i]

print(tot)