#Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

#Appending 1-20 square in a list
def list_():
    list_=[]
    for i in range(1,21):
        list_.append(i**2)

    return list_

#Calling a function and printing it
result=list_()
print("The Result is : ",result)