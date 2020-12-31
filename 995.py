'''
 Write a Python program to scramble the letters of string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']
'''

import random

def shuffle_word(list_):
    list_=list(list_)
    random.shuffle(list_)
    return  ''.join(list_)



list_=['Python', 'list', 'exercises', 'practice', 'solution']

list_output=[shuffle_word(word) for word in list_]
print(list_output)
