''' Write a Python program to remove consecutive duplicates of a given list.
Original list:
[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
After removing consecutive duplicates:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]'''

list_=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
list_output=[]
for i in range(0,len(list_)):
    if list_[i]==list_[i-1]:
        pass
    else:
        list_output.append(list_[i])
print(list_output)