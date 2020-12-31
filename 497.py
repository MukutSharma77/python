'''Fix the Error: Value vs. Reference Types
Create a function that returns True if two lists contain identical values, and False otherwise.
check_equals([1, 2], [1, 3]) ➞ False
check_equals([1, 2], [1, 2]) ➞ True
check_equals([4, 5, 6], [4, 5, 6]) ➞ True
check_equals([4, 7, 6], [4, 5, 6]) ➞ False'''

list1=[1,2,3]
list2=[1,2,6]
print(list1==list2)