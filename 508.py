'''Verbed Nouns
Create a function that ends the first word of a phrase with "ed", essentially verbifying a noun.
Examples
verbify("cheese burger") ➞ "cheesed burger"
verbify("salt water") ➞ "salted water"
verbify("orange juice") ➞ "oranged juice"
verbify("shredded cheese") ➞ "shredded cheese"'''


string='salt water'.split(' ')

if string[0][-1]=='e':
    string[0]=string[0]+'d'
else:
    string[0] = string[0] + 'ed'
print(' '.join(string))