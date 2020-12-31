#Check whether the binary representation of a given number is a palindrome or not in Python

num=9
num_=num
string=''
while num:
    if num % 2 == 0 or num % 2 == 1:
        string+=str(num%2)

    num//=2

if string==string[::-1]:
    print(f"Yes the Binary number of {num_} is palindrome")
else:
    print("Not a palindrome")
