'''Smooth Sentences
Carlos is a huge fan of something he calls smooth sentences. A smooth sentence is one where the last letter of each word is identical to the first letter the following word.
The following would be a smooth sentence: "Carlos swam masterfully." Since "Carlos" ends with an "s" and swam begins with an "s" and swam ends with an "m" and masterfully begins with an "m".
Create a function that determines whether the input sentence is a smooth sentence, returning a boolean value True if it is, False if it is not.
Examples
is_smooth("Marta appreciated deep perpendicular right trapezoids") ➞ True
is_smooth("Someone is outside the doorway") ➞ False
is_smooth("She eats super righteously") ➞ True
'''

sentence="Someone is outside the doorway".split(" ")

count=0

for i in range(len(sentence)):
    if i < len(sentence)-1:
        if sentence[i][-1]==sentence[i+1][0]:

            count+=1

if count==len(sentence)-1:
    print(True)
else:
    print(False)