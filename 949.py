'''Write a Python program to convert a pair of values into a sorted unique array
Original List:  [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
Output :
Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  '''


lst= [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
output_lst=[j for i in lst for j in i]
output_lst=list(set(output_lst))
output_lst.sort()
print(output_lst)