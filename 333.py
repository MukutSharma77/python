'''Given a string, first turn each letter into its ASCII char code.
example:<br><br>
`
'ABC' --> x=65, y=66, z=67 --> '656667'''

string="Mukut"
string2=''


for i in string:
    string2+=str(ord(i))
print(string2)