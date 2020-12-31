#Please write assert statements to verify that every number in the list  is same

#List

list=[2,2,2,2,2,2,2,2]


#if the length of list is equal to occurnece of index 0 than all the element are same else not
if list.count(list[0]) == len(list):
    print("Yes all the element in a list is same")
else:
    print("No Not all the element in the list is same")

