'''Ones, Threes and Nines (Version #2)
Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:
"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends).
Examples
ones_threes_nines(10) ➞ "nines:1, threes:0, ones:1"
ones_threes_nines(15) ➞ "nines:1, threes:2, ones:0"
ones_threes_nines(22) ➞ "nines:2, threes:1, ones:1"'''

def ones_threes_nines(num):

    nine=num//9
    num=num-(9*nine)
    print('nines:',nine,end=" ")
    three=num//3
    num=num-(3*three)
    print('three:',three,end=" ")
    num=num//1
    print('ones:',num,end=" ")
    print()


ones_threes_nines(10)
ones_threes_nines(15)
ones_threes_nines(22)