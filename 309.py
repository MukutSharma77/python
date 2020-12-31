'''Is the Last Character an N?
Create a function that takes a string (a random name). If the last character of the name is an "n", return True, otherwise return False.
Examples
is_last_character_n("Aiden") ➞ True
is_last_character_n("Piet") ➞ False
'''

string='Aiden'
if string[-1]=='n':
    print(True)
else:
    print(False)
