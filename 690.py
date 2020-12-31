'''Card Counting (BlackJack)
In BlackJack, cards are counted with -1, 0, 1 values:
2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the list of cards provided.
Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1
count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6
count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5'''

lst=["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]
tot=0
for i in lst:
    if type(i)==int and i>=2 and i <=6:
        tot+=1

    elif type(i)==int and i>=7 and i <=9:
        tot+=0

    else:
        tot-=1
print(tot)