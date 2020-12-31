'''Oddly or Evenly Positioned
Create a function that returns the characters from a list or string r on odd or even positions, depending on the specifier s. The specifier will be "odd" for items on odd positions (1, 3, 5, ...) and "even" for items on even positions (2, 4, 6, ...).
Examples
char_at_pos([2, 4, 6, 8, 10], "even") ➞ [4, 8]
# 4 & 8 occupy the 2nd & 4th positions
char_at_pos("EDABIT", "odd") ➞ "EAI"
# "E", "A" and "I" occupy the 1st, 3rd and 5th positions
char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd") ➞ ["A", "B", "T", "A", "I", "Y"]'''


def char_at_pos(str_,order):
    lst=[]
    if  order=='even':
        for i in range(1,len(str_),2):
            lst.append(str_[i])
    else:
        for i in range(0,len(str_),2):
            lst.append(str_[i])

    print(lst)




char_at_pos([2, 4, 6, 8, 10], "even")
char_at_pos("EDABIT", "odd")
char_at_pos(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "odd")