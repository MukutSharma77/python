'''Reverse Words Starting With a Particular Letter
Write a function that reverses all the words in a sentence that start with a particular letter.
Examples
special_reverse("word searches are super fun", "s")
➞ "word sehcraes are repus fun"
special_reverse("first man to walk on the moon", "m")
➞ "first nam to walk on the noom"
special_reverse("peter piper picked pickled peppers", "p")
➞ "retep repip dekcip delkcip sreppep"'''

string="first man to walk on the moon".split(' ')
ch='m'
str_=''

for i in string:

    if i[0]==ch:
        str_+=i[::-1]+" "
    else:
        str_+=i+" "

print(str_)