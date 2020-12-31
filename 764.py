'''Letters Shared Between Two Words
Create a function that returns the number of characters shared between two words.
Examples
shared_letters("apple", "meaty") ➞ 2
# Since "ea" is shared between "apple" and "meaty".
shared_letters("fan", "forsook") ➞ 1
shared_letters("spout", "shout") ➞ 4'''

string1='apple'
string2='meaty'
count=0
for i in string1:
    if i in string2:
        count+=1

print(count)