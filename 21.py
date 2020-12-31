#dictionry of n : n^2 ....till n

#Input a number
num=int(input("Enter Number :   "))

#Empty dictionary and now filling it with loop

nodict={}

for i in range(1,num+1):
    nodict[i] = i**2

print(nodict)