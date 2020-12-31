#Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the values only.


#fuction to add i=i**i til i=20 in a empty dict and printing value

def dict_value():
    dictinary={}
    for i in range(1,21):
        dictinary[i]=i**2

    print("The Values of Dictionary is :   ")
    for i in dictinary.values():
        print(i,end=" ")

dict_value()