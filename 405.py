'''Repeat the Same Item Multiple Times
repeat("edabit", 3) ➞ ["edabit", "edabit", "edabit"]
repeat(13, 5) ➞ [13, 13, 13, 13, 13]
repeat("7", 2) ➞ ["7", "7"]'''


item='7'
time=3
list2=[]
for i in range(time):
    list2.append(item)

print(list2)