'''Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end.
Examples
normalize("CAPS LOCK DAY IS OVER") ➞ "Caps lock day is over!"
normalize("Today is not caps lock day.") ➞ "Today is not caps lock day."'''


def function(string):

    if string.isupper():
        string=string.lower()
        string=string.replace(string[0],string[0].title(),1)
        print(string," !")
    else:
        print(False)


string="CAPS LOCK DAY IS OVER"
function(string)