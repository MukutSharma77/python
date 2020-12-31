'''Write a Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
Original list:
[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
Sort the said mixed list of integers and strings:
[1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']'''


lst_=[19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
int_=[i for i in lst_ if type(i)==int]
str_=[i for i in lst_ if type(i)==str]
int_.sort()
str_.sort()
print(int_+str_)
