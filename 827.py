'''Back and Forth
In a board game, a player may pick up a card with a number of left or right facing arrows, with the number of arrows indicating the number of tiles to move. The player should move either left or right, depending on the arrow's direction.
Given a list of the arrows contained on a player's cards, return a singular string of arrowheads which are equivalent to all of the arrowheads.
Worked Example
calculate_arrowhead(['>>', '<<', '<<<']) ➞ '<<<'
# >> means to move 2 places right
# << means to move 2 places left (cancelling out >>)
# <<< means to move a further 3 places left
# overall, the movement can be written as <<<
Examples
calculate_arrowhead(['>>>>', '<', '<', '<']) ➞ '>'
calculate_arrowhead(['>', '<', '>>', '<', '<<<']) ➞ '<<'
calculate_arrowhead(['>>>', '<<<']) '''

def calculate_arrowhead(lst):
    count_right=0
    count_left=0
    for i in lst:
        if '>' in i:
            count_right+=i.count('>')
        else:
            count_left+=i.count('<')

    if count_right > count_left:
        print('>' * (count_right-count_left))

    elif count_left > count_right:
        print('<' * (count_left-count_right))

    else:
        print("''")


calculate_arrowhead(['>>>>', '<', '<', '<'])
calculate_arrowhead(['>', '<', '>>', '<', '<<<'])
calculate_arrowhead(['>>>', '<<<'])