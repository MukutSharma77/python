'''You're given a string of words. You need to find the word "Nemo", and return a string like this: "I found Nemo at [the order of the word you find nemo]!".
If you can't find Nemo, return "I can't find Nemo :(".
Examples
find_nemo("I am finding Nemo !") ➞ "I found Nemo at 4!"'''

string='do you know namo'.split()

msg=f"I found namo on {string.index('namo') + 1}" if 'namo' in string else "I can't find Nemo :("
print(msg)