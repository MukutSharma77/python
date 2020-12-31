'''Double Letters
Create a function that takes a word and returns True if the word has two consecutive identical letters.
Examples
double_letters("loop") ➞ True
double_letters("yummy") ➞ True
double_letters("orange") ➞ False
double_letters("munchkin") ➞ False'''

def function(word):
    count=0
    for i in range(0,len(word)-1):
        if word[i]==word[i+1]:
            print(True)
            count += 1
            break
        else:
            pass

    if count==0:
        print(False)
    else:
        pass



word=input("Enter Word :   ")
function(word)