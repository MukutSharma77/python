'''Write a Python program to find the difference between consecutive numbers in a given list. Go to the editor
Original list:
[1, 1, 3, 4, 4, 5, 6, 7]
Difference between consecutive numbers of the said list:
[0, 2, 1, 0, 1, 1, 1]
Original list:
[4, 5, 8, 9, 6, 10]
Difference between consecutive numbers of the said list:
[1, 3, 1, -3, 4]'''

list_=[4, 5, 8, 9, 6, 10]
lst2=[]
for i in range(1,len(list_)):
    tot=list_[i]-list_[i-1]
    lst2.append(tot)

print(lst2)