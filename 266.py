'''Change Every Letter to the Next Letter
Write a function that changes every letter to the next letter:
"a" becomes "b"
"b" becomes "c"
"d" becomes "e"
and so on ...
Examples
move("hello") ➞ "ifmmp"'''


string='hello'
next_=' '
for i in string:
    asci_=ord(i)+1
    next_+=chr(asci_)

print(next_)