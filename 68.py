# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

def ev(n):
    if n % 2== 0:
        return n

eve_=list(filter(ev , range(1,21) ))
print(eve_)