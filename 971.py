'''Write a Python program to flatten a given nested list structure.
Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
Flatten list:[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]'''

list_=[0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
list_output=[]
for i in list_:
    if type(i)==list:
        for element in i:
            list_output.append(element)
    else:
        list_output.append(i)

print(list_output)