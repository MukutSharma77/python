'''Number Length Sort
Create a sorting function which sorts numbers not by numerical order, but by number length! This means sorting numbers with the least digits first, up to the numbers with the most digits.
Examples
number_len_sort([1, 54, 1, 2, 463, 2]) ➞ [1, 1, 2, 2, 54, 463]
number_len_sort([999, 421, 22, 990, 32]) ➞ [22, 32, 999, 421, 990]
number_len_sort([9, 8, 7, 6, 5, 4, 31, 2, 1, 3]) ➞ [9, 8, 7, 6, 5, 4, 2, 1, 3, 31]'''

list_=[1, 54, 1, 2, 463, 2]

list1=[]
list2=[]
list3=[]
list4=[]
for i  in list_:
    if len(str(i)) == 1:
        list1.append(i)
    elif len(str(i))==2:
        list2.append(i)

    elif len(str(i))==3:
        list3.append(i)

    else:
        list4.append(i)

print(list1+list2+list3+list4)