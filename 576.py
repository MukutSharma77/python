'''Puzzle Pieces
Write a function that takes two lists and adds the first element in the first list with the first element in the second list, the second element in the first list with the second element in the second list, etc, etc. Return True if all element combinations add up to the same number. Otherwise, return False.
Examples
puzzle_pieces([1, 2, 3, 4], [4, 3, 2, 1]) ➞ True
# 1 + 4 = 5;  2 + 3 = 5;  3 + 2 = 5;  4 + 1 = 5
# Both lists sum to [5, 5, 5, 5]
puzzle_pieces([1, 8, 5, 0, -1, 7], [1, 8, 5, 0, -1, 7]) ➞ True
puzzle_pieces([1, 2], [-1, -1]) ➞ False
puzzle_pieces([9, 8, 7], [7, 8, 9, 10]) ➞ False'''


lst_1=[1,2,3,4]
lst_2=[4,3,2,1]

sum_=0

if len(lst_1)==len(lst_2):

    for i in range(len(lst_2)//2):
        tot1 = 0
        tot2 = 0
        tot1=lst_1[i] + lst_1[((len(lst_1)-1)-i)]
        tot2 = lst_2[i] + lst_2[((len(lst_2)-1) - i)]

        if tot2==tot1:
            sum_+=1


print(sum_==len(lst_2)//2)