#Number of Lists in a List

list1=[[1,2] , ['a' , 'b'] , 'jk',[4,3]]

count=0
for i in list1:
    if str(list1).count('['):
        count+=1

print("List inside the lise is :   ",count-1)