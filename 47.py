'''Accumulating Product
Create a function that takes a list and returns a list of the accumulating product.
Examples
accumulating_product([1, 2, 3, 4]) ➞ [1, 2, 6, 24]
# [1, 2, 6, 24] can be written as [1, 1 x 2, 1 x 2 x 3, 1 x 2 x 3 x 4]'''


#Inputting List and one empty list
list_=[ 1 , 2 , 3 , 4 ]
new_list=[]
tot=1
print("The list is :   ",list_)
#with loop adding values and adding in new list
for i in list_:
    tot*=i
    new_list.append(tot)

print("Result  : ",new_list)