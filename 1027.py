'''Write a Python program to find all index positions of the maximum and minimum values in a given list of numbers.
Original list:
[12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
Index positions of the maximum value of the said list:
[7]
Index positions of the minimum value of the said list:
[3, 11]'''


lst_=[12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
max_=max(lst_)
max_lst=[]
for i in range(len(lst_)):
    if lst_[i]==max_:
        max_lst.append(i)

min_=min(lst_)
min_list=[]
for i in range(len(lst_)):
    if lst_[i]==min_:
        min_list.append(i)

print(max_lst,'\n',min_list)