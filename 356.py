'''
Given two data structures, data1 and data2, return data2 converted to the type of data1.
Examples
convert([1, 2, 4, 8], (7, 8, 9)) ➞ [7, 8, 9]
convert((7, 8, 9), [1, 2, 4, 8]) ➞ (1, 2, 4, 8)
convert([1, 2, 4, 8], {2, 3, 5, 7, 11, 13}) ➞ [2, 3, 5, 7, 11, 13]'''

datas=[1,2,3,4,55]
datas2=(1,2,3)

datas=type(datas2)(datas)
print(datas)