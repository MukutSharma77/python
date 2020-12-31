#Python Program to Print Largest Even and Largest Odd Number in a List

#Inputting list
list_=[12,11,13,17,20,100,113,10]

#Crteating two list in one all even and in anothe all odd from above list
list_eve=[i for i in list_ if i %2== 0]
list_odd=[i for i in list_ if i %2 != 0]

# printing max value from it
print("The Largest even value is :   ",max(list_eve))
print("The Largest odd value is :   ",max(list_odd))