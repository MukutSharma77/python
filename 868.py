'''Vowel to Vowel Links
Given a sentence as str, return true if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
Examples
vowelLinks("a very large appliance") ➞ true
vowelLinks("go to edabit") ➞ true
vowelLinks("an open fire") ➞ false
vowelLinks("a sudden applause") ➞ false'''

def vowelLinks(string):
    string=string.split(' ')
    count=0
    for i in range(1,len(string)):
        if string[i][0] in 'aeiou' and string[i-1][-1] in 'aeiou':
            count+=1
    print(count==1)

vowelLinks("a very large appliance")
vowelLinks("go to edabit")
vowelLinks("an open fire")
vowelLinks("a sudden applause")