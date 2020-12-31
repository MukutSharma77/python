'''Create a function that accepts a string of space separated integers and returns the highest and lowest integers (as a string).
Examples
high_low("1 2 3 4 5") ➞ "5 1"
'''

def function(number):
    maxi=max(number)
    mini=min(number)

    string=maxi+" "+mini
    print(f"\"{string}\"")

number=input("Enter Number comma seprated :   ").split(",")
function(number)