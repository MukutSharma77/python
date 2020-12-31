#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10]. USING LAMABDA


#List 1 to 10

list_=[1,2,3,4,5,6,7,8,9,10]
print("The list is  :  ",list_)

#Filtering all the even number

ev_=list(filter(lambda a:a%2==0,list_))
print("All the even number from above list is :  ",ev_)

#Square of ev_ list by map and using lambda
ev_sq=list(map(lambda a:a**2,ev_))
print("Teh square of even number from list :   ",ev_sq)

