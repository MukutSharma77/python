'''
Remove the letters abc
Create a function that will remove the letters a, b and c from the words. If the word has no a, b, c letters, return None
Examples
remove_abc("This might be a bit hard") ➞ This might e  it hrd
remove_abc("hello world!") ➞  None'''

def function(string):
    count=0
    for i in string:
        if i=='a' or i=='b' or i=='c':
            string=string.replace(i,"")
            count+=1
        else:
            pass

    if count==0:
        print("None")
    else:
        print(string)
string="This might be a bit hard"
function(string)