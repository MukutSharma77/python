'''Capitalize by ASCII
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"
ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"
ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."'''

string="to be or not to be!"

str_=''

for i in string:
    if i.isalpha():
        if ord(i) % 2==0:
            str_+=i.upper()
        else:
            str_+=i
    else:
        str_+=i

print(str_)