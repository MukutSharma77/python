'''Box Completely Filled?
Create a function that checks if the box is completely filled with the asterisk symbol *.
Examples
completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
]) ➞ True
completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
]) ➞ False
completely_filled([
  "###",
  "#*#",
  "###"
]) ➞ True
completely_filled([
  "##",
  "##"
]) ➞ True'''


def completely_filled(mat):

    count=0
    for i in range(1,len(mat)-1):
       if mat[i][1:-1] != '*' * (len(mat)-2):
            count+=1

    print(count==0)






completely_filled([
  "#####",
  "#***#",
  "#***#",
  "#***#",
  "#####"
])
completely_filled([
  "#####",
  "#* *#",
  "#***#",
  "#***#",
  "#####"
])
completely_filled([
  "###",
  "#*#",
  "###"
])
completely_filled([
  "##",
  "##"
])