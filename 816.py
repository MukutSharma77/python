'''Collatz Conjecture
A Collatz sequence is generated like this. Start with a positive number. If it's even, halve it. If it's odd, multiply it by three and add one. Repeat the process with the resulting number. The Collatz Conjecture is that every sequence eventually reaches 1 (continuing past 1 just results in an endless repeat of the sequence 4, 2, 1).
The length of the sequence from starting number to 1 varies widely.
Create a function that takes a number as an argument and returns a tuple of two elements — the number of steps in the Collatz sequence of the number, and the highest number reached.
Examples
collatz(2) ➞ (2, 2)
# seq = [2, 1]
collatz(3) ➞ (8, 16)
# seq = [3, 10, 5, 16, 8, 4, 2, 1]
collatz(7) ➞ (17, 52)
# seq = [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
collatz(8) ➞ (4, 8)
# seq = [8, 4, 2, 1]'''


def collatz(num):
    lst=[num]
    # print(lst)
    while True:
        if num == 1:
            break
        else:
            if num%2==0:
                num//=2
            else:
                num=num*3 + 1
            lst.append(num)
    print((len(lst),max(lst)))

collatz(2)
collatz(3)
collatz(7)
collatz(8)