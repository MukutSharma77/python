'''Two Lists inside a List to One

Programmer Pete is trying to turn two lists inside one list into one without messing the order of the list nor the type and because he's pretty advanced he made it without blinking but I want you to make it too.
Examples
one_list([[1, 2], [3, 4]]) ➞ [1, 2, 3, 4]
one_list([["a", "b"], ["c", "d"]]) ➞ ["a", "b", "c", "d"]
one_list([[True, False], [False, False]]) ➞ [True, False, False, False]'''

list1=['a','b']
list2=['c','d']


for i in list2:
    list1.append(i)

print(list1)