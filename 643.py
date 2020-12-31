'''Functioninator 8000
Create a function that takes a single word string and does the following:
Concatenates inator to the end if the word ends with a consonant, otherwise, concatenate -inator instead.
Adds the word length of the original word to the end, supplied with "000".
The examples should make this clear.
Examples
inator_inator("Shrink") ➞ "Shrinkinator 6000"
inator_inator("Doom") ➞ "Doominator 4000"
inator_inator("EvilClone") ➞ "EvilClone-inator 9000"'''

string="Doom"

if string[-1] in 'aeiou':
    print(string+'-inator '+str(len(string)*1000))
else:
    print(string+'inator '+str(len(string)*1000))
