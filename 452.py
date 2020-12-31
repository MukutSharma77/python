'''Is the Average of All Elements a Whole Number?
Create a function that takes a list as an argument and returns True or False depending on whether the average of all elements in the list is a whole number or not.
Examples
is_avg_whole([1, 3]) ➞ True
is_avg_whole([1, 2, 3, 4]) ➞ False
is_avg_whole([1, 5, 6]) ➞ True
is_avg_whole([1, 1, 1]) ➞ True
is_avg_whole([9, 2, 2, 5]) ➞ False
'''


list_=[9,2,2,5]
print(sum(list_)%len(list_)==0)