'''Wrap Around
Create a function to reproduce the wrap around effect shown:
Examples
wrap_around("Hello, World!", 2) ➞ "llo, World!He"
wrap_around("From what I gathered", -4) ➞ "eredFrom what I gath"
wrap_around("Excelsior", 30) ➞ "elsiorExc"
wrap_around("Nonscience", -116) ➞ "cienceNons"'''

def wrap_around(string, idx):
        print(string[idx%len(string):] + string[:idx%len(string)])


wrap_around("Hello, World!", 2)
wrap_around("From what I gathered", -4)
wrap_around("Excelsior", 30)
wrap_around("Nonscience", -116)