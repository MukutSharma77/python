''' Write a Python program to find the difference between elements (n+1th - nth) of a given list of numeric values.Original list:
diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
diff([2, 4, 6, 8])
Output:
[1, 1, 1, 1, 1, 1, 1, 1, 1]
[2, 2, 2]'''

def diff(lst):
    lst_output=[ ]
    for i in  range(1,len(lst)):
        lst_output.append(lst[i]-lst[i-1])

    print(lst_output)


diff([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
diff([2, 4, 6, 8])
