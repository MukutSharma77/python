'''Compounding Letters
Create a function that takes a string and returns a new string with each new character accumulating by +1. Separate each set with a dash.
Examples
accum("abcd") ➞ "A-Bb-Ccc-Dddd"
accum("RqaEzty") ➞ "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") ➞ "C-Ww-Aaa-Tttt"'''

string='RqaEzty'
str_=''
for i in range(len(string)):
    str_+=string[i].upper()+string[i]*i+'-'

print(str_[:-1])