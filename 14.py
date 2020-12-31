#Check if a Number is a Palindrome

#Inputting a number
num=int(input("Enter Number :   "))

#Checking number palindrome or not making a reverse of input with string[]
num_=str(num)
if num == int(num_[::-1]):
    print("Yes number is palindrome\n",num,"  =  ",num_[::-1])

else:
    print("Not a palindrome \n",num,"  !=  ",num_[::-1])