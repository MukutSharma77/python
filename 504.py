'''Vowel Sandwich
Create a function which validates whether a 3 character string is a vowel sandwich. In order to have a valid sandwich, the string must satisfy the following rules:
The first and last characters must be a consonant.
The character in the middle must be a vowel.
Examples
is_vowel_sandwich("cat") ➞ True
is_vowel_sandwich("ear") ➞ False
is_vowel_sandwich("bake") ➞ False
is_vowel_sandwich("try") ➞ False'''


string='ear'.lower()

if len(string)==3:
    if (string[1]=='a' or string[1]=='e' or string[1]=='i' or string[1]=='o' or string[1]=='u') and (string[0] not in 'aeiou'):
        print(True)
    else:
        print(False)
else:
    print(False)
