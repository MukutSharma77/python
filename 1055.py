'''Write a Python program to convert a given list of strings into list of lists.
Original list of strings:
['Red', 'Maroon', 'Yellow', 'Olive']
Convert the said list of strings into list of lists:
[['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]'''




lst_=['Red', 'Maroon', 'Yellow', 'Olive']
lst_output=[]

for i in lst_:
    lsti=[]
    for j in i:
        lsti.append(j)
    lst_output.append(lsti)

# print(lst_output)

print(lst_output)