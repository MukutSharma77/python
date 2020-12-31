'''Rhyme Time
Create a function that returns True if two lines rhyme and False otherwise. For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
Examples
does_rhyme("Sam I am!", "Green eggs and ham.") ➞ True
does_rhyme("Sam I am!", "Green eggs and HAM.") ➞ True
# Capitalization and punctuation should not matter.
does_rhyme("You are off to the races", "a splendid day.") ➞ False
does_rhyme("and frequently do?", "you gotta move.") ➞ False
'''

def does_rhyme(str1,str2):
    str1=str1.lower()
    str2=str2.lower()
    str2=str2.replace('.','')
    str1=str1.replace('!','')
    str1=str1.split(' ')
    str2=str2.split(' ')
    # print(str1,str2)
    print(str1[-1]==str2[-1][1:])

does_rhyme("Sam I am!", "Green eggs and ham.")
does_rhyme("Sam I am!", "Green eggs and HAM.")
does_rhyme("You are off to the races", "a splendid day.")
does_rhyme("and frequently do?", "you gotta move.")
