'''Write a Python program to extract the nth element from a given list of tuples.
Original list:
[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]
Extract nth element ( n = 0 ) from the said list of tuples:
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
Extract nth element ( n = 2 ) from the said list of tuples:
[99, 96, 94, 98]'''

def extract(lst,idx):
    lst_ouput=[]
    for i in lst:
        for j in i:
            if i.index(j)==idx:
                lst_ouput.append(j)

    print(lst_ouput)
extract([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] , 0)
extract([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] , 2)