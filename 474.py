'''Determine If Two Numbers Add up to a Target Value
Given two unique integer lists a and b, and an integer target value v, create a function to determine whether there is a pair of numbers that add up to the target value v, where one number comes from one list a and the other comes from the second list b.
Return True if there is a pair that adds up to the target value and False otherwise.
Examples
sum_of_two([1, 2], [4, 5, 6], 5) ➞ True
sum_of_two([1, 2], [4, 5, 6], 8) ➞ True
sum_of_two([1, 2], [4, 5, 6], 3) ➞ False
sum_of_two([1, 2], [4, 5, 6], 9) ➞ False'''

list1=[1,2]
list2=[4,5,6]
v=9
count=0
for i in list1:
    for j in list2:
        tot=0
        tot=i+j
        if tot==v:
            print(True)
            count+=1

if count==0:
    print(False)