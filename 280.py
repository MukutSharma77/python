'''
Write a function that reverses all the words in a sentence that start with a particular letter.
Examples
special_reverse("word searches are super fun", "s")
➞ "word sehcraes are repus fun"'''

def function(string):
    string_new=''
    for i in string:
        # print(i[0])
        if i[0]=='s':
            string_new+=" " + i[::-1]
        else:
            string_new+=" " + i
    print(string_new)

string='word searches are super fun'.lower().split(' ')
function(string)
# print(string)