''' Write a Python program to display vertically each element of a given list, list of lists. Go to the editor
Original list:
['a', 'b', 'c', 'd', 'e', 'f']
Display each element vertically of the said list:
a
b
c
d
e
f
Original list:
[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
Display each element vertically of the said list of lists:
1 4 7
2 5 3
5 8 6'''


lst_=['a', 'b', 'c', 'd', 'e', 'f']
for i in lst_:
    print(i)

print()

lst=[[1, 2, 5], [4, 5, 8], [7, 3, 6]]
for a,b,c in (zip(*lst)):
    print(a,b,c)