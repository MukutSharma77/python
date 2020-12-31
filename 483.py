'''Find the Bomb
Create a function that finds the word "bomb" in the given string. If found, return "Duck!!!", otherwise, return "There is no bomb, relax.".
Examples
bomb("There is a bomb.") ➞ "Duck!!!"
bomb("Hey, did you think there is a bomb?") ➞ "Duck!!!"
bomb("This goes boom!!!") ➞ "There is no bomb, relax."'''

string="Hey, did you think there is a bomb?".lower()
if 'bomb' in string:
    print('"Duck!!!"')
else:
    print('"There is no bomb, relax."')