'''Write a Python program to extract a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Extract 1st column:
[1, 2, 1]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Extract 3rd column:
[3, -5, 1]'''

def lst_extract(lst_ , idx):
    lst_output=[]
    for i in lst_:
        for j in range(len(i)):
            if j==idx-1:
                lst_output.append(i[j])

    print(lst_output)


lst_extract([[1, 2, 3], [2, 4, 5], [1, 1, 1]],1)
lst_extract([[1, 2, 3], [-2, 4, -5], [1, -1, 1]],3)