'''Write a Python program to find the maximum and minimum values in a given list within specified index range.
Original list:
[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
Index range:
3 to 8
Maximum and minimum values of the said given list within index range:
(5, 0)'''


lst_=[4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]
idx_from=3
idx_to=8
lst_output=lst_[idx_from : idx_to]
print((max(lst_output) , min(lst_output)))