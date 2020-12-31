'''Words With Duplicate Letters
Given a common phrase, return False if any individual word in the phrase contains duplicate letters. Return True otherwise.
Examples
no_duplicate_letters("Fortune favours the bold.") ➞ True
no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") ➞ True
no_duplicate_letters("Look before you leap.") ➞ False
# Duplicate letters in "Look" and "before".
no_duplicate_letters("An apple a day keeps the doctor away.") ➞ False
# Duplicate letters in "apple", "keeps", "doctor", and "away".'''


def no_duplicate_letters(string):
    count=0
    string=string.split(' ')
    stru=""
    for i in string:
        for j in i:
            if i.count(j)==1:
                stru+=j
    # print(stru)
    string=''.join(string)
    # print(string)
    print(stru==string)
no_duplicate_letters("Fortune favours the bold.")
no_duplicate_letters("You can lead a horse to water, but you can't make him drink.")
no_duplicate_letters("Look before you leap.")
no_duplicate_letters("An apple a day keeps the doctor away.")