'''Switcharoo
Create a function that takes a string and returns a new string with its first and last characters swapped, except under three conditions:
If the length of the string is less than two, return "Incompatible.".
If the argument is not a string, return "Incompatible.".
If the first and last characters are the same, return "Two's a pair.".
Examples
flip_end_chars("Cat, dog, and mouse.") ➞ ".at, dog, and mouseC"
flip_end_chars("ada") ➞ "Two's a pair."
flip_end_chars("Ada") ➞ "adA"
flip_end_chars("z") ➞ "Incompatible."
flip_end_chars([1, 2, 3]) ➞ "Incompatible."'''

string="Cat, dog, and mouse."

if len(string) < 2 or string[0]==string[-1] or type(string) is not str :
    print('Incompaitable')

else:
    string2=string[-1] + string[1:-1] +string[0]
    print(string2)