# list comprehension to get each odd number in a list

#Inputting numbers Commo seprated
numbers=input("Enter Number Commo seprated :    ").split(",")
print("The inputed number is :   ", (",").join(numbers))

#appending another list by numbers of only odd numbers

list_=[int(i) for i in numbers if int(i) % 2 !=0 ]
print(list_)
