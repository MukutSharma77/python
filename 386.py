'''Skip the Drinks with Too Much Sugar
The function skip_the_sugar() takes in a list of drinks. Make sure the function only returns a list of drinks with no sugar in it or a little bit of sugar.
Drinks that contain too much sugar (in this challenge) are:
Cola
Fanta
Examples
skip_the_sugar(["fanta", "cola", "water"]) ➞ [water]
skip_the_sugar(["fanta", "cola"]) ➞ []'''

list_=["fanta", "cola", "water"]
lsit2=['cola','fanta']
list3=[]
for i in list_:
    if i not in lsit2:
        list3.append(i)
print(list3)