'''Write a Python program to print a nested lists (each list on a new line) using the print() function.
colors = [['Red'], ['Green'], ['Black']]
Output:
['Red']
['Green']
['Black'] '''

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(i) for i in colors]))