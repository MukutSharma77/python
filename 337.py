'''
Create a function to concatenate two integer lists which have common eleement.
Examples
concat([1, 3, 5,8], [1, 3 2, 6, 8]) ➞ [1, 3,  8]
'''


def concatenate(list1,list2):
    list3=list1+list2
    list_=[]
    for i in list3:
        if i in list2 :
            if i in list1:
                list_.append(i)
    print(sorted(list(set(list_))))


list1=[1,3,5,8]
list2=[1,3,2,6,8]
concatenate(list1,list2)