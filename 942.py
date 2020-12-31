'''
 Write a Python program to change the position of every n-th value with the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
'''

lst_=[0,1,2,3,4,5]
for i in range(1,len(lst_),2):
    lst_[i-1] , lst_[i] = lst_[i] , lst_[i-1]

print(lst_)