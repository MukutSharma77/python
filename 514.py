'''Tuck in List
Create a function that takes two lists and insert the second list in the middle of the first list.
Examples
tuck_in([1, 10], [2, 3, 4, 5, 6, 7, 8, 9]) ➞ [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuck_in([15,150], [45, 75, 35]) ➞ [15, 45, 75, 35, 150]
tuck_in([[1, 2], [5, 6]], [[3, 4]]) ➞ [[1, 2], [3, 4], [5, 6]]'''

list1=[[1, 2] , [5,6]]
list2=[[3,4]]

list2.insert(0,list1[0])
list2.append(list1[-1])
print(list2)