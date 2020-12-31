'''Orthogonal Vector
Create a function that takes two vectors as lists and checks if the two vectors are orthogonal or not. The return value is boolean. Two vectors first and second are orthogonal if their dot product is equal to zero.
Examples
is_orthogonal([1, 2], [2, -1]) ➞ True
is_orthogonal([3, -1], [7, 5]) ➞ False
is_orthogonal([1, 2, 0], [2, -1, 10]) ➞ True'''

lst1=[3,-1]
lst2=[7,5]

lst3=[]
for i in range(len(lst1)):
    lst3.append(lst1[i]*lst2[i])

# print(lst3)
print(0==sum(lst3))