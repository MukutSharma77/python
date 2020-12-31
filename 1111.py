'''The Kempner Function
The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose factorial is exactly divided by the number.
kempner(6) ➞ 3
1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0
kempner(10) ➞ 5
1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0'''

def kempner(num):
    for i in range(2,num+1):
        tot=1
        for j in range(1,i+1):
            tot*=j
        if tot % num==0:
            print(i)
            break


kempner(6)
kempner(10)