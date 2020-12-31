'''Write a Python program to check if the elements of a given list are unique or not.
Original list:
unique([1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17])
unique([2, 4, 6, 8, 10, 12, 14])
Output :
False
True'''

def unique(lst):
    count=0
    for i in lst:
        if lst.count(i)==1:
            count+=1

    print(count==len(lst))



unique([1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17])
unique([2, 4, 6, 8, 10, 12, 14])
