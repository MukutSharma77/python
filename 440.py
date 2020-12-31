'''Minimum Removals to Make Sum Even
Create a function that returns the minimum number of elements removed to make the sum of all elements in a list even.
Examples:
minimum_removals([1, 2, 3, 4, 5]) ➞ 1
minimum_removals([5, 7, 9, 11]) ➞ 0
minimum_removals([5, 7, 9, 12]) ➞ 1
'''

list_=[5,7,9,11]
print(sum(list_)%2)