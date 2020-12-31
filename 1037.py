'''Write a Python program to get the frequency of the elements in a given list of lists.
Original list of lists:
[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
Frequency of the elements in the said list of lists:
{1: 1, 2: 3, 3: 1, 4: 1, 5: 2, 6: 1, 7: 1, 8: 1, 9: 1}'''

lst=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
lst_concate=[j for i in lst for j in i]
dict_={}
for i in lst_concate:
    if i not in dict_:
        dict_[i] = lst_concate.count(i)

print(dict_)