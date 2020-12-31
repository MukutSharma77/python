# Read Print Prime Numbers in a Range using Sieve of Eratosthenes

#Inputting a number
num=int(input("Enter Number :  "))

#prime number start with 2 so the condition is that number should equal or greater than 3
if num >= 2:
    #We want the number between 2 to given number
    for i in range(2,num+1):
        count=0
        #Checking every element by loop is is it prime
        for j in range(2,i):
            if i % j == 0:
                count+=1
            else:
                pass
        #printing if it is prime
        if count==0:
            print(i,end="  ")
        else:
            pass
