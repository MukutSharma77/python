'''Common Divisor of List
Write a function that returns the greatest common divisor of all list elements. If the greatest common divisor is 1, return 1.
Examples
GCD([10, 20, 40]) ➞ 10
GCD([1, 2, 3, 100]) ➞ 1
GCD([1024, 192, 2048, 512]) ➞ 64'''

def GCD(lst):
    output=[]
    for i in lst:
        for j in range(2,i+1):
            if i % j==0:
                output.append(j)
    count=0
    ch=''
    for i in output:
        if output.count(i)==len(lst):
            ch=i
            count+=1
    
    if count==0:
        print(1)
    else:
        print(ch)

GCD([10, 20, 40])
GCD([1, 2, 3, 100])
GCD([1024, 192, 2048, 512])