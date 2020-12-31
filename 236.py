# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

list_=[1,2,3,5,4,5]

if list_ == list(set(list_)):
    print(True)

else:
    print(False)