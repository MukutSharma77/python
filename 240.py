#Write a Python program to identify nonprime numbers between 1 to 100 (integers). Print the nonprime numbers.

for i in range(2,100):
    for j in range(2,i):
        if i % j == 0:
            print(format(i),end=" ")
            break
