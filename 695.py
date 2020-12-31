'''Applying Discounts
Create a function that applies a discount d to every number in the list.
Examples
get_discounts([2, 4, 6, 11], "50%") ➞ [1, 2, 3, 5.5]
get_discounts([10, 20, 40, 80], "75%") ➞ [7.5, 15, 30, 60]
get_discounts([100], "45%") ➞ [45]'''

lst=[100]
per='45%'
per=int(per.strip('%'))

lst2=[]
for i in lst:
    lst2.append(i*per/100)

print(lst2)