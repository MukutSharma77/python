'''Factorials
Create a function that filters out factorials from a list. A factorial is a number that can be represented in the following manner:
Examples
filter_factorials([1, 2, 3, 4, 5, 6, 7]) ➞ [1, 2, 6]
filter_factorials([1, 4, 120]) ➞ [1, 120]
filter_factorials([8, 9, 10]) ➞ []'''


def filter_factorials(lst):
    fct_=[]
    for i in lst:
        tot=1
        for j in range(1,i+1):
            tot*=j
            if tot ==i:
                fct_.append(tot)
                break
    print(fct_)




filter_factorials([1, 2, 3, 4, 5, 6, 7])
filter_factorials([1, 4, 120])
filter_factorials([8, 9, 10])