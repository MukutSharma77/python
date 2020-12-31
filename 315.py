'''AND, OR and NOT
Continue to write the three logic gates: AND, OR and NOT.
Examples
AND(1, 1) ➞ 1
AND(0, 0) ➞ 0
OR(1, 0) ➞ 1
OR(1, 1) ➞ 1
NOT(0) ➞ 1
NOT(1) ➞ 0'''

def and_():
    num1=int(input("Enter number 1  :  "))
    num2 = int(input("Enter number 2  :  "))

    if num1==1 and num2==1:
        print('1 and 1 = 1')


    elif num1==0 and num2==1:
        print('0 and 1 = 0')


    elif num1==1 and num2==0:
        print('1 and 0 = 0')

    elif num1==0 and num2==0:
        print("'0 and 0 =  0")

    else:
        print("Inavlid Input")


def or__():
    num1 = int(input("Enter number 1  :  "))
    num2 = int(input("Enter number 2  :  "))

    if num1 == 1 and num2 == 1:
        print('1 OR 1 = 1')


    elif num1 == 0 and num2 == 1:
        print('0 OR 1 = 1')


    elif num1 == 1 and num2 == 0:
        print('1 OR 0 = 1')

    elif num1 == 0 and num2 == 0:
        print("'0 or  0 =  0")

    else:
        print("Inavlid Input")


def not__():
    num1 = int(input("Enter number 1  :  "))

    if num1 == 1 :
        print('1 NOT = 0')
    elif num1==0:
        print('0 not = 1')

    else:
        print('Inval;id ')

and_()
or__()

not__()