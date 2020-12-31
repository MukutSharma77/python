#Write a Python program to accept a filename from the user and print the extension of that.
'''Sample filename : abc.java
Output : java'''

file_name=input("Enter Name :   ")

if '.' in file_name:
    print("Extension of a file is  :  ",end="  ")
    idx=file_name.index('.')
    for i in range(idx+1,len(file_name)):
        print(file_name[i],end="")

else:
    print("invalid input")