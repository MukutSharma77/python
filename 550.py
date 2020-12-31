'''Reverse the Order of Words with Five Letters or More
Write a function that takes a string of one or more words as an argument and returns the same string, but with all five or more letter words reversed. Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.
Examples
reverse("Reverse") ➞ "esreveR"
reverse("This is a typical sentence.") ➞ "This is a lacipyt .ecnetnes"
reverse("The dog is big.") ➞ "The dog is big."'''

string="This is a typical sentence.".split(" ")
str_=''
for i in string:
    if len(i) >= 5:
        str_+=i[::-1]+" "
    else:
        str_+=i+" "

print(str_)