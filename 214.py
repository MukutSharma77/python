#Write a Python program to create a histogram from a given list of integers

list_=[1,5,3,4,2]

for i in list_:
    for j in range(0,i):
        print("#",end=" ")
    print()