'''Write a Python program to find the list in a list of lists whose sum of elements is the highest.
Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
Expected Output: [10, 11, 12]'''

list_=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

max_=list_[0]

for i in list_:
    if sum(i)>sum(max_):
        max_=i
print(max_)