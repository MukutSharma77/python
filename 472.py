'''Count the Capital Letters
Given a string of letters, how many capital letters are there?
Examples
capital_letters("fvLzpxmgXSDrobbgMVrc") ➞ 6
capital_letters("JMZWCneOTFLWYwBWxyFw") ➞ 14
capital_letters("mqeytbbjwqemcdrdsyvq") ➞ 0'''

string="fvLzpxmgXSDrobbgMVrc"

count_uppper=0
for i in string:
    if i.isupper():
        count_uppper+=1
print(count_uppper)