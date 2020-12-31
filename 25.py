import  math
'''
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30
input comma seprated
'''

def formula(numbers):
    c=50
    h=30

    for i in numbers:
        i=int(i)
        x=math.sqrt((2*c*i)//h)
        print(int(x.__round__(0)))



#inputting value and calling function  t
print("You can insert one or more than one value (COMMA SEPRATED)")
numbers=input("Enter Numbers  :    ").split(",")
formula(numbers)



