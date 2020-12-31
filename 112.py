#write a program that prints out all the elements of the list that are less than 5.

#inputting list from user sking user how many values he need to add in list
tot_element=int(input("Enter Number of element in list   :    "))

#Running loops tot_element time to sore value and appending it
i=1
list_=[]
while i <= tot_element:
    x=int(input(f'Enter element {i}  :     '))
    list_.append(x)
    i+=1
print("This inputted list is  :           ",list_)

#Checking is the no is less than 5 in a list if yes than printing it
count_=0
for i in list_:
    if i <= 5:
        print(i,end="  ")
        count_+=1
    else:
        pass

if count_>0:
    pass
else:
    print("No Number Less than 5")