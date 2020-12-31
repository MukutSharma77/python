'''Number of Stickers
Given an n * n * n Rubik's cube, return the number of individual stickers that are needed to cover the whole cube.
Examples
how_many_stickers(1) ➞ 6
how_many_stickers(2) ➞ 24
how_many_stickers(3) ➞ 54
Notes
Keep in mind there are 6 faces to keep track of.
Expect only positive whole numbers.'''

num=3

if type(num)==int:
    print((num**2)*6)

else:
    print('Invalid')