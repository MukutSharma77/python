'''Capitalize the Last Letter
Create a function that capitalizes the last letter of every word.
Examples
cap_last("hello") ➞ "hellO"
cap_last("My Name Is Edabit") ➞ "MY NamE IS EdabiT"
cap_last("HELp THe LASt LETTERs CAPITALISe") ➞ "HELP THE LAST LETTERS CAPITALISE"'''

def cap_last(string):
    string=string.split(' ')
    for i in string:
        print(i[:-1]+i[-1].upper(),end=" ")
    print()


cap_last("hello")
cap_last("My Name Is Edabit")
cap_last("HELp THe LASt LETTERs CAPITALISe")