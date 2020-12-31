'''Write a function that takes an ordered list of numbers (a list
where the elements are in order from smallest to largest) and
another number. The function decides whether or not the given
number is inside the list and returns (then prints) an
appropriate boolean.'''


#Fuction to cheack wheather x present in a list or not
def search(list_,x):
    if x in list_:
        print(f"Yes {x} is present in a list")
    else:
        print(f"{x} is not present")





#Inputting list askking user how many values he need to store in list
length=int(input("Enter the Length of list  :    "))

# using loop length time and entering values and appendiong it
list_=[]
for i in range(1,length+1):
    x=int(input(f"Enter Value {i}    :   "))
    list_.append(x)

list_.sort()
print("Inputted list is :  ",list_)

 #Searching number storing in x
x=int(input("Serach number from list :   "))
search(list_,x)
