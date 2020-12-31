'''The Farm Problem
In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
chickens = 2 legs
cows = 4 legs
pigs = 4 legs
The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
Examples
animals(2, 3, 5) ➞ 36
animals(1, 2, 3) ➞ 22
'''

chicken=int(input("Enter number of Chicken :  "))
cow=int(input("Enter number of Cows :  "))
pig=int(input("Enter number of Pigs :  "))

print("Total legs :    ",(cow*4)+(chicken * 2) + (pig*4))