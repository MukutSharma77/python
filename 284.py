'''Given a word, write a function that returns the first index and the last index of a character.
Examples
char_index("hello", "l") ➞ [2, 3]
# The first "l" has index 2, the last "l" has index 3.
'''

def function(string):
    search=input("Enter search :   ")
    if search in string:
        print(string.index(search))
        print(string.rindex(search))
string='hello'
function(string)