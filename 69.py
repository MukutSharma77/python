#Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10]. USING LAMBDA

#List of 1 to 10
list_=[1,2,3,4,5,6,7,8,9,10]
print("List is : ",list_)

#using filter and lambda for even number from list
list=list(filter(lambda a : a % 2 ==0 ,list_))


print("Even number from list :  ",list)