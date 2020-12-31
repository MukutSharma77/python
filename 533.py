'''Split a String Based on Vowels and Consonants
Write a function that takes a string, breaks it up and returns it with vowels first, consonants second. For any character that's not a vowel (like special characters or spaces), treat them like consonants.
Examples
split("abcde") ➞ "aebcd"
split("Hello!") ➞ "eoHll!"
split("What's the time?") ➞ "aeieWht's th tm?"
Notes
Vowels are a, e, i, o, u.'''

string="What's the time?"
vowel=''
consonent=''
symbol=''
for i in string:
    if i in 'aeiou' or i in 'AEIOU':
        vowel+=i
    else:
        consonent+=i

print(vowel+consonent)