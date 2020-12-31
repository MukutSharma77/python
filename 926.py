'''Write a Python program to find the highest 3 values in a dictionary
my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}'''

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}
value_lst=[i for i in my_dict.values()]
value_lst=list(set(value_lst))
value_lst.sort()


print("The Largest three value is :   ",value_lst[-3:])