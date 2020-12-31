'''Python has a logical operator and. The and operator takes two boolean values, and returns True if both values are True.
Examples
And(True, False) ➞ False
And(True, True) ➞ True
And(False, True) ➞ False
And(False, False) ➞ False'''

def and_(string1,string2):
    if string1==True and string2==True:
        print(True)

    else:
        print(False)



string1=True
string2=True
and_(string1,string2)