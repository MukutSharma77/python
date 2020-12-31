#Print all Integers that Aren't Divisible by Either 2 or 3 and Lie between 1 and 50.

#using for loop to display the numbers which is not divisible by 2 or 3

for i in range(1,51):
    if i % 2 ==0 or i % 3 == 0:
        pass
    else:
        print(i, end=" ")
