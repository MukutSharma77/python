#Python Program that Displays which Letters are in the First String but not in the Second

string1="mkutlp"
string2='tanu'

string_=''
for i in string1:
    if i not in string2:
        string_+=i

print("Letters which are in string1 but not in string2   :    ",string_)