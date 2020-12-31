'''Vowel Replacer
Create a function that replaces all the vowels in a string with a specified character.
Examples
replace_vowels("the aardvark", "#") ➞ "th# ##rdv#rk"
replace_vowels("minnie mouse", "?") ➞ "m?nn?? m??s?"
replace_vowels("shakespeare", "*") ➞ "sh*k*sp**r*"
'''

string="the aardvark"
sym='?'

for i in string:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        string=string.replace(i,sym)



print(string)