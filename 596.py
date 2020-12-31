'''N-Sized Parts
Create a function that divides a string into parts of size n.
Examples
partition("chew", 2) ➞ ["ch", "ew"]
partition("thematic", 4) ➞ ["them", "atic"]
partition("c++", 2) ➞ ["c+", "+"]
'''

string="c++"
num=2
if num<=len(string):
    list_=[string[:num], string[num:]]

print(list_)