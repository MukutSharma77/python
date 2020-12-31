#Python Program to Find the Sum of First N Natural Numbers

num=int(input("Enter Number :   "))
tot=0
for i in range(1,num+1):
    tot+=i

print(f"THe sum of {num} natural number   :       {tot} ")