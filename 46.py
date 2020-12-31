'''Create a function that takes in a list and returns a list of the accumulating sum.
Examples
accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
# [1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]'''


#Inputting List and one empty list
list_=[ 1 , 2 , 3 , 4 ]
new_list=[]
tot=0
print("The list is :   ",list_)
#with loop adding values and adding in new list
for i in list_:
    tot+=i
    new_list.append(tot)

print("Result  : ",new_list)