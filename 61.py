# Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included)


#Fuction to append element in list than converting it in tuple
def tup():
    tuple_=[]
    for i in range(1,21):
        tuple_.append(i)

    tuple_=tuple(tuple_)
    print(tuple_)

#calling a function
tup()