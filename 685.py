'''Check if the String is a Palindrome
A palindrome is a word, phrase, number or other sequence of characters which reads the same backward or forward, such as madam or kayak.
Write a function that takes a string and determines whether it's a palindrome or not. The function should return a boolean (True or False value).
Examples
is_palindrome("Neuquen") ➞ True
is_palindrome("Not a palindrome") ➞ False
is_palindrome("A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!") ➞ True
Notes
Should be case insensitive.
Special characters (punctuation or spaces) should be ignored.
'''

string='A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!'.lower()
string=string.replace(' ','')
string=string.replace(',','')
string=string.replace('!','')
string=string.replace('.','')
string=string.replace('-','')
print(string==string[::-1])
