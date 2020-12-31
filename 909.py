'''
Write a Python program to get the maximum and minimum value in a dictionary
{'x':500, 'y':5874, 'z': 560}
'''

dict_={'x':500, 'y':5874, 'z': 560}
lst_val=[i for i in dict_.values()]
print('Maximum number is :  ',max(lst_val))
print('Minimum number is :  ',min(lst_val))