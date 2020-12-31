'''reate a function which adds spaces before every capital in a word. Uncapitalize the whole string afterwards.
Examples
cap_space("helloWorld") ➞ "hello world"
cap_space("iLoveMyTeapot") ➞ "i love my teapot"'''

string='iLoveMyTeapot'

list_=[]
for i in string:
    list_.append(i)

string_=""

for i in list_:
    if i.isupper():
        string_+=" "+i

    else:
        string_+=i

print(string_.lower())