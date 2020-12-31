'''
Create a function that takes a string and replaces the vowels with another character.
a = 1
e = 2
i = 3
o = 4
u = 5
Examples
replace_vowel("karachi") ➞ "k1r1ch3"'''


def function(string):
    dict_={
        'a' : '1',
        'e' : '2',
        'i' : '3',
        'o' : '4',
        "u" : '5'
        }
    string_=""
    for i in string:
        if i in dict_:

            string_+=dict_[i]
        else:
            string_+=i

    print(string_)





string='karachi'
function(string)