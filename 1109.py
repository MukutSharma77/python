'''Shared vs. Unique Letters
Create a function that takes in two words as input and returns a list of three elements, in the following order:

Shared letters between two words.
Letters unique to word 1.
Letters unique to word 2.
Each element should have unique letters, and have each letter be alphabetically sorted.

Examples
letters("sharp", "soap") ➞ ["aps", "hr", "o"]
letters("board", "bored") ➞ ["bdor", "a", "e"]
letters("happiness", "envelope") ➞ ["enp", "ahis", "lov"]
letters("kerfuffle", "fluffy") ➞ ["flu", "ekr", "y"]
letters("match", "ham") ➞ ["ahm", "ct", ""]'''


def letters(str1 , str2):
    lst=[]
    string1=''
    for i in str1:
        if i in str2:
            string1+=i

    lst.append(string1)

    string1=''
    for i in str1:
        if i not in str2:
            string1+=i

    lst.append(string1)

    string1=''
    for i in str2:
        if i not in str1:
            string1+=i

    lst.append(string1)
    print(lst)

letters("sharp", "soap")
letters("board", "bored")
letters("happiness", "envelope")
letters("kerfuffle", "fluffy")
letters("match", "ham")