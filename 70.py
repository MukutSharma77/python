# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10]. USING LAMBDA

#list 1 to 10
list_=[1,2,3,4,5,6,7,8,9,10]
print("The list is :  ",list_)

#Using lambda and map functin for the square of each element from list

list=list(map(lambda a:a**2,list_))
print("Sqaure of above list :  ",list)