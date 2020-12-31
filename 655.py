'''Find the Highest Integer in the List Using Recursion
Create a function that finds the highest integer in the list using recursion.
Examples
find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99
find_highest([0, 12, 4, 87]) ➞ 87
find_highest([8]) ➞ 8'''

def find_highest(lst):
    lst.sort()
    return lst[-1]

lst=[-1, 3, 5, 6, 99, 12, 2]
output=find_highest(lst)
print(output)