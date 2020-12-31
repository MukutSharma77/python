'''
Write a Python program to remove duplicate dictionary from a given list.Original list with duplicate dictionary:
[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
After removing duplicate dictionary of the said list:
[{'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]
'''

lst=[{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

lst_put=[]
for i in lst:
    if i not in lst_put:
        lst_put.append(i)

print(lst_put)

