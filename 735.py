'''Reverse the Odd Length Words
Given a string, reverse all the words which have odd length. The even length words are not changed.
Examples
reverse_odd("Bananas") ➞ "sananaB"
reverse_odd("One two three four") ➞ "enO owt eerht four"
reverse_odd("Make sure uoy only esrever sdrow of ddo length")
➞ "Make sure you only reverse words of odd length"'''

string="One two three four".split(' ')
str_=[]
for i in string:

    if len(i) % 2==0:
        str_.append(i)
    else:
        str_.append(i[::-1])


print(' '.join(str_))