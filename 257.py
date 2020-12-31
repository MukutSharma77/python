'''Given two lists, return whether the two lists are opposites of each other. That means that both lists are comprised only from elements a and b and that the
occurences of these elements are swapped between the two lists.
Examples
is_anti_list(['1', '0', '0', '1'], ['0', '1', '1', '0']) ➞ True
is_anti_list(['apples', 'bananas', 'bananas'], ['bananas', 'apples', 'apples']) ➞ True
is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]) ➞ False'''


list1=[3.14, True, 3.14]
list2=[3.14, 3.14, True]

if sorted(list1)==sorted(list2):
    print(True)
else:
    print(False)