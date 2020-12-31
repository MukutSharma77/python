'''Write a Python program to find common element(s) in a given nested lists.
Original lists:
[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
Common element(s) in nested lists:
[18, 12]'''


lst=[[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]

output=[]
for i in lst[0]:
    if i in lst[1] and i in lst[2]:
        output.append(i)

print(output)