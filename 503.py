'''War of Numbers
There's a great war between the even and odd numbers. Many numbers already lost their life in this war and it's your task to end this. You have to determine which group is larger: the even, or the odd. The larger group wins.
Create a function that takes a list of integers and sum up the even and odd numbers seperately and then substract the smaller one from the bigger one. Return the substraction.
Examples
war_of_numbers([2, 8, 7, 5]) ➞ 2
# 2 + 8 = 10
# 7 + 5 = 12
# 12 - 10
war_of_numbers([12, 90, 75]) ➞ 27
war_of_numbers([5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]) ➞ 168
'''

list_=[5, 9, 45, 6, 2, 7, 34, 8, 6, 90, 5, 243]

tot_ev=0
tot_od=0

for i in list_:
    if i % 2==0:
        tot_ev+=i
    else:
        tot_od+=i

if tot_ev>=tot_od:
    print(tot_ev-tot_od)
else:
    print(tot_od-tot_ev)