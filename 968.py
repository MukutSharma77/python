'''Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]'''

list_=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
uni_list=[]
for i in list_:
    if i not in uni_list:
        uni_list.append(i)


print(uni_list)