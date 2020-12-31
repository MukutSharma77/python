'''
Write a function that transforms all letters from [a, m] to 0 and letters from [n, z] to 1 in a string.
'''
def function(string):
    binary=''
    for i in string:
        if ord(i) >= 97 and ord(i) <= 110  :
            binary+='0'

        elif ord(i) >= 65     and    ord(i) <= 78:
            binary+='0'
        else:
            binary+='1'

    print(binary)
string=input("Enter String :   ")
function(string)