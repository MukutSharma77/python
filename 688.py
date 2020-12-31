'''Characters in Shapes
Create a function that counts how many characters make up a rectangular shape. You will be given a list of strings.
Examples
count_characters([
  "###",
  "###",
  "###"
]) ➞ 9
count_characters([
  "22222222",
  "22222222",
]) ➞ 16
count_characters([
  "------------------"
]) ➞ 18
count_characters([]) ➞ 0
count_characters(["", ""]) ➞ 0
'''

lst=[]
tot=0
for i in range(len(lst)):
    tot+=len(lst[i])

print(tot)