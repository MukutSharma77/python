'''Remove Repeated Letters
Create a function that replaces all consecutively repeated letters in a word with single letters.
Examples
remove_repeats("aaabbbccc") ➞ "abc"
remove_repeats("bookkeeper") ➞ "bokeper"
remove_repeats("nananana") ➞ "nananana"'''

string='aaabbbccc'
str_=''
for i in range(len(string)):
    if string[i]==string[i-1]:
        pass
    else:
        str_+=string[i]

print(str_)