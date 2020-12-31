#Create a function that returns True if the first list is a subset of the second. Return False otherwise.

list1=[1,2,3,100]
list2=[1,2,3,4,4,5,6,7,7,3]


count=0
for i in list1:
    if i in list2:
        count+=1

if count==len(list1):
    print(True)
else:
    print(False)