'''From A to Z
Given a string indicating a range of letters, return a string which includes all the letters in that range, including the last letter. Note that if the range is given in capital letters, return the string in capitals also!
Examples
gimme_the_letters("a-z") ➞ "abcdefghijklmnopqrstuvwxyz"
gimme_the_letters("h-o") ➞ "hijklmno"
gimme_the_letters("Q-Z") ➞ "QRSTUVWXYZ"
gimme_the_letters("J-J") ➞ J"
'''

def gimme_the_letters(str_):
    string=''
    # print(ord(str_[0]),ord(str_[-1]))
    for i in range(ord(str_[0]) , ord(str_[-1])+1):
        string+=chr(i)
    print(string)

gimme_the_letters("a-z")
gimme_the_letters("h-o")
gimme_the_letters("Q-Z")
gimme_the_letters("J-J")
