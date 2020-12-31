'''Given a range of first 10 numbers, Iterate from start number to the end number and print the sum of the current number and previous number'''

num=10

for i in range(1,11):
    print(f"Current number is {i} Previous Number {i-1}  : {i+(i-1)}")
