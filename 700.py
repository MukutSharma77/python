'''Amazing Alliteration
Alliteration refers to a sequence of words that begin with the same letter. For this exercise, a sentence is correctly alliterated if all words strictly greater than 3 characters begin with the same letter.
Examples
alliteration_correct("She swam to the shore.") ➞ True
# All words >= 4 letters long begins with "s"
alliteration_correct("Maybel manages money well.") ➞ False
# "well" does not begin with an "m"
alliteration_correct("He helps harness happiness.") ➞ True
alliteration_correct("There are many animals.") ➞ False'''

string="He helps harness happiness.".split(' ')

lst=[i[0] for i in string]
print(lst)
count=0
for i in lst:
    if lst.count(i)==3:
        count+=1


print(count==3)