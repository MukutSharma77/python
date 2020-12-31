'''Reverse and Capitalize
Create a function that takes a string of lowercase characters and returns that string reversed and in upper case.

Examples
reverse_capitalize("abc") ➞ "CBA"

reverse_capitalize("hellothere") ➞ "EREHTOLLEH"

reverse_capitalize("input") ➞ "TUPNI"
'''

string='hellothere'
str_=''

for i in string[::-1]:
    str_+=i

print(str_.upper())