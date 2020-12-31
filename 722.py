'''Subset Validation
Write a function that returns True if all subsets in a list belong to a given set.
Examples
validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True
validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True
validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False
validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False'''

lst1=[[1, 2], [2, 3], [1, 3]]
lst2=[1, 2, 3]
lst3=[]

for i in lst1:
    for j in i:
        lst3.append(j)
# print(lst3)
print(list(set(lst3))==lst2)