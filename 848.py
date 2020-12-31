'''Censor Words from List
Create a function that takes a string txt and censors any word from a given list lst. The text removed must be replaced by the given character char.
Examples
censor_string("Today is a Wednesday!", ["Today", "a"], "-") ➞ "----- is - Wednesday!"
censor_string("The cow jumped over the moon.", ["cow", "over"], "*"), "The *** jumped **** the moon.")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*") ➞ "Why *** the ******* cross the ****?"'''

def censor_string(string,lst,sign):
    string=string.replace('?','')
    string=string.split(' ')
    str_=[]
    for i in string:
        if i in lst:
            str_.append(sign * len(i))
        else:
            str_.append(i)
    print(' '.join(str_))


censor_string("Today is a Wednesday!", ["Today", "a"], "-")
censor_string("The cow jumped over the moon.", ["cow", "over"], "*")
censor_string("Why did the chicken cross the road?", ["Did", "chicken", "road"], "*")