'''Vowel to Vowel Links
Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).
Examples
vowel_links("a very large appliance") ➞ True
vowel_links("go to edabit") ➞ True
vowel_links("an open fire") ➞ False
vowel_links("a sudden applause") ➞ False'''

def vowel_links(string):
    string=string.split(' ')
    count=0
    # print(string)
    for i in range(1, len(string)):
        if string[i - 1][-1] in 'aeiou' and  string[i][0] in 'aeiou':
            count+=1

    if count>=1:
        print(True)
    else:
        print(False)



vowel_links("a very large appliance")
vowel_links("go to edabit")
vowel_links("an open fire")
vowel_links("a sudden applause")