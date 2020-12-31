'''Longest Word
Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word. Characters such as apostophe, comma, period (and the like) count as part of the word (e.g. O'Connor is 8 characters long).
Examples
longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
longest_word("A thing of beauty is a joy forever.") ➞ "forever."
longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"'''

string="Forgetfulness is by all means powerless!".split(' ')
max_=string[1]

for i in string:
    if len(i) > len(max_):
        max_=i

print(max_)

