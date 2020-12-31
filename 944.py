'''Write a Python program to split a list based on first character of word.
Input:
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call'
Output:
a
ask
b
be
c
call
come
d
do
-----
w
want
work    '''



word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

word_ch=[i[0] for i in word_list]
word_ch=list(set(word_ch))
word_ch.sort()
word_list.sort()
for i in word_ch:
    print(i)
    for j in word_list:
        if i==j[0]:
            print(j)

