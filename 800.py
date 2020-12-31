'''Emphasise the Words
The challenge is to recreate the functionality of the title() method into a function called emphasise(). The title() method capitalises the first letter of every word and lowercases all of the other letters in the word.
Examples
emphasise("hello world") ➞ "Hello World"
emphasise("GOOD MORNING") ➞ "Good Morning"
emphasise("99 red balloons!") ➞ "99 Red Balloons!"
'''

def emphasise(string):
    string=string.split(' ')
    for i in string:
        print(i.capitalize(),end=" ")
    print()



emphasise("hello world")
emphasise("GOOD MORNING")
emphasise("99 red balloons!")