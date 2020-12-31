'''Find ASCII Charcode of Inverse Case Character
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97
counterpartCharCode("A") ➞ 97
counterpartCharCode("a") ➞ 65
'''

def counterpartCharCode(chr_):
    if chr_.isupper():
        return ord(chr_.lower())
    else:
        return ord(chr_.upper())
chr_='a'
if len(chr_)==1:
    output=counterpartCharCode(chr_)
    print(output)