'''Find the Largest Even Number
Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in function max() and sorted() are prohibited.
Examples
largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10
largest_even([1, 3, 5, 7]) ➞ -1
largest_even([0, 19, 18973623]) ➞ '''

lst=[3, 7, 2, 1, 7, 9, 10, 13]
msg= list(i for i in lst if i %2==0)
print(max(msg))