'''Find the Bug: Checking Even Numbers
Create a function that takes in an array and returns True if all its values are even, and False otherwise.
Examples
check_all_even([1, 2, 3, 4]) ➞ False
check_all_even([2, 4, 6]) ➞ True
check_all_even([5, 6, 8, 10]) ➞ False
check_all_even([-2, 2, -2, 2]) ➞ True'''

list_=[2,4,6]

list_2=[i for i in list_ if i %2==0]
print(len(list_2)==len(list_))