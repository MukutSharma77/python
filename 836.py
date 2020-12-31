'''Is the Number a Prime? (with a twist)
prime(7) ➞ True
prime(56963) ➞ True
prime(5151512515524) ➞ False
'''

def prime(num):
    i=2
    count=0
    while i<num//2:
        if num % i ==0:
            count+=1
            break
        i+=1
    print(count==0)




prime(7)
prime(56963)
prime(5151512515524)
