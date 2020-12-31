'''Abbreviating a Sentence
Create a function which takes a sentence and returns its abbreviation. Get all of the words over or equal to n characters in length and return the first letter of each, capitalised and overall returned as a single string.
Examples
abbreviate("do it yourself") ➞ "Y"
abbreviate("do it yourself", 2) ➞ "DIY"
# "do" and "it" are included because the second parameter specified that word lengths 2 are allowed.
abbreviate("attention AND deficit OR hyperactivity THE disorder") ➞ "ADHD"
# Words below the default 4 characters are not included in the abbreviation.
abbreviate("the acronym of long word lengths", 5) ➞ "AL"
# "acronym" and "lengths" have 5 or more characters.
Notes
There may not be an argument given for n so set the default to 4.
'''

def abbreviate(string,n=4):
    string=string.split(' ')
    str_=''
    for i in string:
        # print(i)
        if len(i) > 4 or len(i) >= n:
            str_+=i[0].upper()
    print(str_)


abbreviate("do it yourself")
abbreviate("do it yourself", 2)
abbreviate("attention AND deficit OR hyperactivity THE disorder")
abbreviate("the acronym of long word lengths", 5)
