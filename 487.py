'''Find the Index
Create a function that takes a list and a string as arguments and return the index of the string.
Examples
find_index(["hi", "edabit", "fgh", "abc"], "fgh") ➞ 2
find_index(["Red", "blue", "Blue", "Green"], "blue") ➞ 1
find_index(["a", "g", "y", "d"], "d") ➞ 3
find_index(["Pineapple", "Orange", "Grape", "Apple"], "Pineapple") ➞ 0'''

list_=["hi", "edabit", "fgh", "abc"]
idx='fgh'

if idx in list_:
    print(list_.index(idx))
else:
    print('Not present')