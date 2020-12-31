'''Pair Management
Given two arguements, return a list contains these two arguements.
Examples
make_pair(51, 21) ➞[51, 21]
make_pair(512124, 215) ➞[512124, 215]'''

def make_pair(num1,num2):
    list_=[num1,num2]
    return list_

num1=int(input("Enter Number 1 :   "))
num2=int(input("Enter Number 2 :   "))
result=make_pair(num1,num2)
print(result)