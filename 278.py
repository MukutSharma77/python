'''Create a function that takes a string and returns the middle character(s). If the word's length is odd, return the middle character. If the word's length is even, return the middle two characters.
Examples
get_middle("test") ➞ "es"
get_middle("testing") ➞ "t"
'''
def get_middle(string):
    if len(string) % 2 != 0:
        print(string[len(string)//2])
    else:
        print( string[(len(string)//2)-1],string[len(string)//2] )
string="testing"
get_middle(string)