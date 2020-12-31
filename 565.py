'''Remove the letters abc
Create a function that will remove the letters a, b and c from the words. If the word has no a, b, c letters, return None
Examples
remove_abc("This might be a bit hard") ➞ This might e  it hrd
remove_abc("hello world!") ➞  None
remove_abc("") ➞ None
'''

string=""
count=0
str_=''

for i in string:
    if i in 'abc':
        count+=1
    else:
        str_+=i

if count==0:
    print(None)
else:
    print(str_)