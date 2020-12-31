'''Apples and Bananas
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"
vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"
vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"'''

string="stuffed jalapeno poppers"
replace_='e'

string=string.replace('a',replace_)
string=string.replace('e',replace_)
string=string.replace('i',replace_)
string=string.replace('o',replace_)
string=string.replace('u',replace_)
print(string)