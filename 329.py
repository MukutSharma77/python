'''Create a function that returns the string "Burp" with the amount of "r's" determined by the input parameters of the function.
Examples
long_burp(3) ➞ "Burrrp"
long_burp(5) ➞ "Burrrrrp"
long_burp(9) ➞ "Burrrrrrrrrp"
Notes'''


def long_burp(num):
    print('Bu'+ 'r'*num + 'p')

num=int(input("Enter Number  ;  "))
long_burp(num)