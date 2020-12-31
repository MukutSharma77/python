'''Write a Python program to find the maximum and minimum values in a given list of tuples. Original list with tuples:
[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
Maximum and minimum values of the said list of tuples:
(78, 60)'''

list_=[('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]
list_.sort(key=lambda e:e[1])
print((list_[0][1] , list_[-1][1]))