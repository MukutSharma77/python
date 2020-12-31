'''Extending The String
Make two functions:
consonants(word) which returns the number of consonants in a word when called.
vowels(word) which returns the number of vowels in a word when called.
Examples
vowels('Jameel SAEB') ➞ 5
consonants('He|\o mY Fr*end') ➞ 7
consonants("Smithsonian") ➞ 7
vowels("Smithsonian") ➞ 4
Notes
Vowels are: a, e, i, o, u.
Spaces and special character do not count as consonants nor vowels.'''

def vowels(string):
    count=0
    for i in string:
        if i.lower() in 'aeiou':
            count+=1
    print(count)

def consonants(string):
    count=0
    for i in string:
        if i.lower() not in  'aeiou' and i.isalpha():
            count+=1
    print(count)

vowels('Jameel SAEB')
consonants('He|\o mY Fr*end')
consonants("Smithsonian")
vowels("Smithsonian")