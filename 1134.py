'''Almost Palindrome
A string is an almost-palindrome if, by changing only one character, you can make it a palindrome. Create a function that returns True if a string is an almost-palindrome and False otherwise.
Examples
almost_palindrome("abcdcbg") ➞ True
# Transformed to "abcdcba" by changing "g" to "a".
almost_palindrome("abccia") ➞ True
# Transformed to "abccba" by changing "i" to "b".
almost_palindrome("abcdaaa") ➞ False
# Can't be transformed to a palindrome in exactly 1 turn.
almost_palindrome("1234312") ➞ False'''

def almost_palindrome(string):
    str_=string[::-1]

    count=0
    for i in range(0,len(string)):
        if str_[i]==string[i]:
            count+=1

    print(len(string)-2==count)

almost_palindrome("abcdcbg")
almost_palindrome("abccia")
almost_palindrome("abcdaaa")
almost_palindrome("1234312")