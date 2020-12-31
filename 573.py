'''Ranged Reversal
Write a function that reverses the sublist between the start and end index (inclusive). The rest of the list should be kept the same.
Examples
ranged_reversal([1, 2, 3, 4, 5, 6], 1, 3) ➞ [1, 4, 3, 2, 5, 6]
ranged_reversal([1, 2, 3, 4, 5, 6], 0, 4) ➞ [5, 4, 3, 2, 1, 6]
ranged_reversal([9, 8, 7, 4], 0, 0) ➞ [9, 8, 7, 4]'''


def ranged_reversal(lst,start,end_idx):
    lst2=lst[start:end_idx+1]
    lst2.reverse()
    lst2=lst[:start]+lst2+lst[end_idx+1:]
    print(lst2)


lst=[1, 2, 3, 4, 5, 6]
start=1
end_idx=3

ranged_reversal(lst,start,end_idx)