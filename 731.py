'''Scottish Screaming
A strong Scottish accent makes every vowel similar to an "e", so you should replace every vowel with an "e". Additionally, it is being screamed, so it should be in block capitals.
Create a function that takes a string and returns a string.
Examples
to_scottish_screaming("hello world") ➞ "HELLE WERLD"
to_scottish_screaming("Mr. Fox was very naughty") ➞ "MR. FEX WES VERY NEEGHTY"
to_scottish_screaming("Butterflies are beautiful!") ➞ "BETTERFLEES ERE BEEETEFEL!"'''

def to_scottish_screaming(string):
    str_=''
    for i in string:
        if i in 'AEIOU':
            str_+='E'

        else:
            str_+=i
    return str_

string="hello world".upper()
output=to_scottish_screaming(string)
print(output)