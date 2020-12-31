'''You work in a toy car workshop, and your job is to build toy cars from a collection of parts. Each toy car needs 4 wheels, 1 car body, and 2 figures of people to be placed inside. Given the total number of wheels, car bodies and figures available, how many complete toy cars can you make?
Examples
cars(2, 48, 76) ➞ 0
# 2 wheels, 48 car bodies, 76 figures
cars(43, 15, 87) ➞ 10
cars(88, 37, 17) ➞ 8
'''

wheel=int(input("Enter tot number of wheels    :  "))
car_body=int(input("Enter Number of car body   :  "))
fig=int(input("Enter number of figure          :  "))


count=0
while True:
    if wheel>3 and car_body>0 and fig>1:
        wheel=wheel-4
        car_body=car_body-1
        fig=fig-2
        count+=1
    else:
        break

print(count)
