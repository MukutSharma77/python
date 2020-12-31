'''Check a sentence contain all the vowel if yes Print(‘Accepted’) else print(‘Missing vowel’)'''

string='aboeieucd'
string=string.lower()
dict_={
    'a' : 1,
    'e' : 1,
    'i' : 1,
    'o' : 1,
    'u' : 1
}

store_vowel=''

for i in string:
    if i in dict_ and i not in store_vowel:
        store_vowel+=i


if ''.join(sorted(store_vowel))=='aeiou':
    print('Accepetd')
else:
    print('Missing variable')