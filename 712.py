'''The Fifth Argument
Create a function (named fifth) that takes some arguments and returns the type of the fifth argument. In case the arguments were less than 5, return "Not enough arguments".
Examples
fifth(1, 2, 3, 4, 5) ➞ int
fifth("a", 2, 3, [1, 2, 3], "five") ➞ str
fifth() ➞ "Not enough arguments"'''

def fifth(*args):
    if len(args)==5:
        print(type(args[4]).__name__)
    else:
        print('Not enough arguement')
fifth("a", 2, 3, [1, 2, 3], "five")