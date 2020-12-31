# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.

import random

list_=['a', 'e', 'i', 'o', 'u']

msg=random.shuffle(list_)

print(''.join(list_))
