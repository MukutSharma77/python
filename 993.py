'''Write a Python program to sort each sublist of strings in a given list of lists.
Original list:
[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
After sorting each sublist of the said list of lists:
[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]'''


list_=[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
for i in list_:
    i.sort()

print(list_)