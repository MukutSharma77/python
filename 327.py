'''The challenge is to try and fix this buggy code, given the inputs True and False. See the examples below for the expected output.
Examples
has_bugs(True) ➞ "sad days"
has_bugs(False) ➞ "it's a good day"'''

input_=input("Enter True or False   :  ").lower()

if input_=='true':
    print("Sad days")
elif input_=='false':
    print("it's a good day")
else:
    print("Wrong Input")