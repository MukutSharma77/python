'''House of Cards
The image below shows a sequence of larger and larger houses of cards, with the total number of cards included for each:
House of Cards
Given the tower height n, return the number of cards needed to construct a full house of cards.
Examples
cards_needed(3) ➞ 15
cards_needed(4) ➞ 26
cards_needed(0) ➞ 0
Notes
The height should always be equal or greater than 0. Return "invalid" if the value given doesn't abide by this rule.
 n*(3*n + 1)/2'''

num=4
print(int(num*(3 * num + 1)/2))