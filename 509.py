'''Upper or Lower Case
Return the smallest number of steps it takes to convert a string entirely into uppercase or entirely into lower case, whichever takes the fewest number of steps. A step consists of changing one character from lower to upper case, or vice versa.
Examples
steps_to_convert("abC") ➞ 1
# "abC" converted to "abc" in 1 step
steps_to_convert("abCBA") ➞ 2
# "abCBA" converted to "ABCBA" in 2 steps
steps_to_convert("aba") ➞ 0
steps_to_convert("abaCCC") ➞ 3'''

string="abaCCC"

upper_ch=0
lower_ch=0

for i in string:
    if i.isupper():
        upper_ch+=1
    else:
        lower_ch+=1

count=0
if upper_ch>lower_ch:
    for i in string:
        if i.islower():
            count+=1

else:
    for i in string:
        if i.isupper():
            count+=1

print(count)