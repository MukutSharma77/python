'''
Create a function that takes a number as an argument. Add up all the numbers from 1 to the number you passed to the function. For example, if the input is 4 then your function should return 10 because 1 + 2 + 3 + 4 = 10.
Examples
add_up(4) ➞ 10
add_up(13) ➞ 91'''


def add_up(num):
    tot=0
    for i in range(0,num+1):
        tot+=i

    print(tot)


num=int(input("Enter Number :   "))
add_up(num)