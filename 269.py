'''Write a function that moves all elements of one type to the end of the list.'''

list_=["a", "a", "a", "b"]

no=input("Move to :  ")

if no.isdigit():
    if int(no) in list_:
        no=int(no)
        for i in list_:
            if i == no:
                list_.remove(i)
                list_.append(i)
    else:
        print("Number not found")

elif no.isalpha():
    if no in list_:
        for i in list_:
            if i == no:
                list_.remove(i)
                list_.append(i)
    else:
        print("Letter not found")

    print(list_)