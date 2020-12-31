'''Find the First Non-Repeated Character
Create a function that accepts a string as an argument and returns the first non-repeated character.
Examples
first_non_repeated_character("g") ➞ "g"
first_non_repeated_character("it was then the frothy word met the round night") ➞ "a"
first_non_repeated_character("the quick brown fox jumps then quickly blows air") ➞ "f"
first_non_repeated_character("hheelloo") ➞ False
first_non_repeated_character("") ➞ False
'''

string="the quick brown fox jumps then quickly blows air"

count=0
for i in string:
    if string.count(i)==1:
        count+=1
        print(i)
        break


if count==0 or len(string)==0:
    print(False)