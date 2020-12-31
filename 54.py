#Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

#Function for add i : i**i in a empty Dictionary with help of loop
def dict_():
    dictionary={}
    for i in range(1,4):
        dictionary[i] = i**2

    return  dictionary

#Calling a function and printing it
result=dict_()
print("Output is :    ",result)