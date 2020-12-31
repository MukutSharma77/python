'''Define a function that can accept an integer number as input
and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
'''

#Funtion to check whether a number is even or odd
def ev_odd(num):
    if num % 2 == 0:
        print("The Given number is EVEN")
    else:
        print("The Given number is ODD")



#Inputing number and calling a function
num=int(input("Enter Number :   "))
ev_odd(num)