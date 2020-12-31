'''Write a Python program to map two lists into a dictionary.
Input :
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
Output : {'red': '#FF0000', 'green': '#008000', 'blue': '#0000FF'}'''


keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

my_dict_=dict(zip(keys,values))
print(my_dict_)