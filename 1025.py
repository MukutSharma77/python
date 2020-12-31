'''Write a Python program to count the same pair in three given lists.
Original lists:
[1, 2, 3, 4, 5, 6, 7, 8]
[2, 2, 3, 1, 2, 6, 7, 9]
[2, 1, 3, 1, 2, 6, 7, 9]
Number of same pair of the said three given lists:
3'''

list1=[1, 2, 3, 4, 5, 6, 7, 8]
list2=[2, 2, 3, 1, 2, 6, 7, 9]
list3=[2, 1, 3, 1, 2, 6, 7, 9]

list_check=list(zip(list1,list2,list3))
count=0
for i in list_check:
    if len(i)==i.count(i[0]):
        count+=1

print(count)