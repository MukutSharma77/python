'''Extend the Vowels
Create a function that takes a word and extends all vowels by a number num.
Examples
extend_vowels("Hello", 5) ➞ "Heeeeeelloooooo"
extend_vowels("Edabit", 3) ➞ "EEEEdaaaabiiiit"
extend_vowels("Extend", 0) ➞ "Extend"'''

def extend_vowels(string,num):
    for i in string:
        if i.lower() in 'aeiou' :
            print(i*(num+1),end="")
        else:
            print(i,end="")
    print()


extend_vowels("Hello", 5)
extend_vowels("Edabit", 3)
extend_vowels("Extend", 0)