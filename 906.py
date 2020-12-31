'''
Write a Python program to check whether a given key already exists in a dictionary.
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
is_key_present(5)--> True
is_key_present(9)--> False'''

def is_key_present(n):
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
    print(n in d.keys())


is_key_present(5)
is_key_present(9)