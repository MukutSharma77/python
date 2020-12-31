'''Beginning and End Pairs
Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
Examples
pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
pairs([]) ➞ []'''

def pairs(lst):
    output=[]
    for i in range(0,len(lst)//2):
        lst_=[lst[0] , lst[-1]]
        lst.pop()
        lst.pop(0)
        output.append(lst_)

    if len(lst)==1:
        lsting=[lst[0] , lst[0]]
        output.append(lsting)
    print(output)
pairs([1, 2, 3, 4, 5, 6, 7])
pairs([1, 2, 3, 4, 5, 6])
pairs([5, 9, 8, 1, 2])
pairs([])
