'''Don't Roll Doubles!
John is playing a dice game. The rules are as follows.
Roll two dice.
Add the numbers on the dice together.
Add the total to your overall score.
Repeat this for three rounds.
But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!
Create a function that takes in a list of tuples as input, and return John's score after his game has ended.
Examples
dice_game([(1, 2), (3, 4), (5, 6)]) ➞ 21
dice_game([(1, 1), (5, 6), (6, 4)]) ➞ 0
dice_game([(4, 5), (4, 5), (4, 5)]) ➞ 27'''

def dice_game(lst_):
    tot=0
    c=0
    for i in lst_:
        if i[0]==i[1]:
            print(0)
            c+=1
            break
        else:
            tot+=i[0]+i[1]

    if c==0:
        print(tot)

dice_game([(1, 2), (3, 4), (5, 6)])
dice_game([(1, 1), (5, 6), (6, 4)])
dice_game([(4, 5), (4, 5), (4, 5)])