'''
Atbash Cipher
The Atbash cipher is an encryption method in which each letter of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
Create a function that takes a string and applies the Atbash cipher to it.
Examples
atbash("apple") ➞ "zkkov"
atbash("Hello world!") ➞ "Svool dliow!"
atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
'''

def atbash(string):
    str_=' '
    A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Z = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
    a='abcdefghijklmnopqrstuvwxyz'
    z='zyxwvutsrqponmlkjihgfedcba'
    for i in string:
        if i.islower():
            str_+=z[a.index(i)]
        elif i.isupper():
            str_+=Z[A.index(i)]

    print(str_)
atbash("apple")
atbash("Hello world!")
atbash("Christmas is the 25th of December")