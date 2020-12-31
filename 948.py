'''
Write a Python program to generate groups of five consecutive numbers in a list.
List is ;   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
output
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

'''

list_=[i for i in range(1,26)]
print('List is ;  ',list_)
list_output=[ ]
for i in range(0,len(list_),5):
    list_output.append(list_[i:i+5])

print("Output :  ",end="   ")
print(list_output)