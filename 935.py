'''
 Write a Python function that takes two lists and returns True if they have at least one common member.
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))
output :
True
False
'''


def common_data(lst1,lst2):
    lst1=set(lst1)
    lst2=set(lst2)
    intersction=list(lst1&lst2)
    return  len(intersction )>=1




print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9]))
