'''Which Number Is Not like the Others?
Create a function that takes a list of numbers and return the number that's unique.
Examples
unique([3, 3, 3, 7, 3, 3]) ➞ 7
unique([0, 0, 0.77, 0, 0]) ➞ 0.77
unique([0, 1, 1, 1, 1, 1, 1, 1]) ➞ 0'''

list_=[0, 0, 0.77, 0, 0]
for i in list_:
    if list_.count(i)==1:
        print(i)