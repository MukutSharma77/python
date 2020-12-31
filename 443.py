'''Lowercase, Uppercase or Mixed?
Create a function which returns "upper" if all the letters in a word are uppercase, "lower" if lowercase and "mixed" for any mix of the two.
Examples
get_case("whisper...") ➞ "lower"
get_case("SHOUT!") ➞ "upper"
get_case("Indoor Voice") ➞ "mixed"
'''

string='SHOUT!'

if string.islower():
    print('lower')
elif string.isupper():
    print('upper')
else:
    print('mixed')