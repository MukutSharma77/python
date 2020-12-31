'''Remove None from a List
Create a function to remove all None values from a list.
Examples
remove_none(["a", None, "b", None]) ➞ ["a", "b"]
remove_none([None, None, None, None, None]) ➞ []
remove_none([7, 8, None, 9]) ➞ [7, 8, 9]
'''

list_=["a", None, "b", None]
list2=[i for i in list_ if i != None]
print(list2)