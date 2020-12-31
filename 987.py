'''Write a Python program to Zip two given lists of lists. Original lists:
[[1, 3], [5, 7], [9, 11]]
[[2, 4], [6, 8], [10, 12, 14]]
Zipped list:
[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]'''

list1=[[1, 3], [5, 7], [9, 11]]
list2=[[2, 4], [6, 8], [10, 12, 14]]

list3=[]

for i in range(len(list1)):
    list_=[]
    for val1 in list1[i]:
        list_.append(val1)

    for val2 in list2[i]:
        list_.append(val2)

    list3.append(list_)

print(list3)
