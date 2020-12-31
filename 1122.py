'''Generating Words from Names
Write a function that returns True if a given name can generate an array of words.
Examples
anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True
anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True
anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
'''



def anagram(str_ , lst):
    str_=str_.lower()

    storing=' '
    for i in lst:
        for j in i:
            storing+=j

    print(sorted(str_)==sorted(storing))


anagram("Justin Bieber", ["injures", "ebb", "it"])
anagram("Natalie Portman", ["ornamental", "pita"])
anagram("Chris Pratt", ["chirps", "rat"])
anagram("Jeff Goldblum", ["jog", "meld", "bluffs"])
