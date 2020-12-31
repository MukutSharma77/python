'''Multiply by Length
Create a function to multiply all of the values in a list by the amount of values in the given list.
Examples
MultiplyByLength([2, 3, 1, 0]) ➞ [8, 12, 4, 0]
MultiplyByLength([4, 1, 1]) ➞ ([12, 3, 3])
MultiplyByLength([1, 0, 3, 3, 7, 2, 1]) ➞  [7, 0, 21, 21, 49, 14, 7]'''

list_=[2,3,1,0]
list2=[]
for i in list_:
    list2.append(i*len(list_))
print(list2)