'''
Create a function to concatenate two integer lists which have different eleement.
Examples
concat([1, 3, 5,8], [1, 3 2, 6, 8]) ➞ [5,2,6]'''

list1=[1,3,5,8]
list2=[1,3,2,6,8]

list1=set(list1)
list2=set(list2)
list3=list(list1.union(list2))
print(list3)
for i in list3:
    if i not in list2:
        print(i,end=" ")
    elif i not in list1:
        print(i,end=" ")
    else:
        pass