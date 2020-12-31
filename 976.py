''' Write a Python program to decode a run-length encoded given list.
Original encoded list:
[[2, 1], 2, 3, [2, 4], 5, 1]
Decode a run-length encoded said list:
[1, 1, 2, 3, 4, 4, 5, 1]'''

list_=[[2, 1], 2, 3, [2, 4], 5, 1]
lst_output=[]
for i in list_:
    if type(i)==list:
        for k in range(i[0]):
            lst_output.append(i[1])

    else:
        lst_output.append(i)

print(lst_output)