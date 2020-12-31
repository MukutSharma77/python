'''Remove Duplicates from a List
Create a function that takes a list of items, removes all duplicate items and returns a new list in the same sequential order as the old list (minus duplicates).
Examples
remove_dups([1, 0, 1, 0]) ➞ [1, 0]
remove_dups(["The", "big", "cat"]) ➞ ["The", "big", "cat"]
remove_dups(["John", "Taylor", "John"]) ➞ ["John", "Taylor"]
'''

lst=[1,0,1,0]
lst2=[]
for i in lst:
    if i not in lst2:
        lst2.append(i)

print(lst2)