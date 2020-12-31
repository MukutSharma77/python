'''Unmix My Strings
lPaeesh le pemu mnxit ehess rtnisg! Oh, sorry, that was supposed to say: Please help me unmix these strings!
Somehow my strings have all become mixed up; every pair of characters has been swapped. Help me undo this so I can understand my strings again.
Examples
unmix("123456") ➞ "214365"
unmix("hTsii  s aimex dpus rtni.g") ➞ "This is a mixed up string."
unmix("badce") ➞ "abcde"
'''

def unmix(str_):
    string=''

    for i in range(1,len(str_),2):
        string+=str_[i]+str_[i-1]
    if len(str_)%2==0:
        print(string)
    else:
        print(string+str_[-1])
unmix("123456")
unmix("hTsii  s aimex dpus rtni.g")
unmix("badce")