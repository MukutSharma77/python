'''Create a function that changes specific words into emoticons. Given a sentence as a string, replace the words smile, grin, sad and mad with their corresponding emoticons.
word	emoticon
smile	:D
grin	:)
sad	:(
mad	:P
Examples
emotify("Make me smile") ➞ "Make me :D"
emotify("Make me grin") ➞ "Make me :)"
emotify("Make me sad") ➞ "Make me :("'''

def function_(string):
    if string[2]=='smile':
        print("Make me :D")
    elif string[2]=='grin':
        print('Make me :)')
    elif string[2]=='sad':
        print("Make me :(")
    else:
        print("Invalid")
string="Make me grin".split(' ')
function_(string)