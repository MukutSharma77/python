'''
Write a Python program to check whether a list contains a sublist
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))

Output:
True                                                                                                         False
False
'''

def is_Sublist(lst1,lst2):
    count=0
    for i in range(1,len(lst1)):
        if lst1[i:i+2]==lst2:
            count+=1

    return count>0

a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))
