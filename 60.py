# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
#  Then the function needs to print all values except the first 5 elements in the list.


#Appending 1-20 square in a list
def list_():
    list_=[]
    for i in range(1,21):
        list_.append(i**2)

    return list_[5:]


#Calling a function and printing it
result=list_()
print("The Result is : ",result)