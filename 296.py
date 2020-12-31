'''Given a list of numbers, return a list which contains all the even numbers in the orginal list, which also have even indices.
Examples
get_only_evens([1, 3, 2, 6, 4, 8]) ➞ [2, 4]
get_only_evens([0, 1, 2, 3, 4]) ➞ [0, 2, 4]'''

list_=[0, 1, 2, 3, 4]
list2=[]
for i in list_:
    if list_.index(i) % 2==0:
        if i % 2==0:
            list2.append(i)

print(list2)