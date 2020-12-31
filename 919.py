'''
Remove empty list from a list
List is :   [1, 2, [], 3, 4, [], 8, 9]
Output :    [1, 2, 3, 4, 8, 9]
'''

lst_=[1,2,[],3,4,[],8,9]
lst_output=[i for i in lst_ if type(i)!=list]
print("List is :  ",lst_)
print("Output :   ",lst_output)