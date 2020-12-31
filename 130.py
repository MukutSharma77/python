#Create a program that asks the user for a number and then prints out
# a list of all the divisors of that number.


#Inputting a number by user and creating an empty list

number=int(input("Enter Number :    "))
list_=[]

#Checking 1 to number is devsible by a nukmber if yes appending it in list
for i in range(1,number+1):
    if number%i==0:
        list_.append(i)
    else:
        pass

print("The divisible by input number is :  ",list_)

