'''Transform into a List with No Duplicates
A set is a collection of unique items. A set can be formed from a list from removing all duplicate items.
[1, 3, 3, 5, 5, 5]
# original list
[1, 3, 5]
# original list transformed into a set
Create a function that sorts a list and removes all duplicate items from it.
Examples
setify([1, 3, 3, 5, 5]) ➞ [1, 3, 5]
setify([4, 4, 4, 4]) ➞ [4]'''

lst=[1, 3, 3, 5, 5, 5]
print(list(set(lst)))
