'''Syncopated Rhythm
Syncopation means an emphasis on a weak beat of a bar of music; most commonly, beats 2 and 4 (and all other even-numbered beats if applicable).
s is a line of music, represented as a string, where hashtags # represent emphasized beats. Create a function that returns if the line of music contains any syncopation.
Examples
has_syncopation(".#.#.#.#") ➞ True
# There are Hash signs in the second, fourth, sixth and
# eighth positions of the string.
has_syncopation("#.#...#.") ➞ False
# There are no Hash signs in the second, fourth, sixth or
# eighth positions of the string.
has_syncopation("#.#.###.") ➞ True
# There are Hash signs in the sixth positions of the string.'''

string="#.#.###."
count=0
for i in range(len(string)):
    if string[1]=='#' or string[3]=='#' or string[5]=='#' or string[7]=='#':
        print(True)
        count+=1
        break

if count==0:
    print(False)
else:
    pass

