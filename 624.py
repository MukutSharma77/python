'''Invert Colors
Create a function that inverts the rgb values of a given tuple.
Examples
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.
color_invert((0, 0, 0)) ➞ (255, 255, 255)
color_invert((165, 170, 221)) ➞ (90, 85, 34)'''

tup=(165, 170, 221)
tup_=[]

for i in tup:
    tup_.append(255-i)

print(tuple(tup_))