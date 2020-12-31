'''Sum of Prime Numbers
Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.
Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17
sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87
sum_primes([]) ➞ None'''

def sum_primes(lst):
    tot_prime=[]

    for i in lst:
        if i > 1:
            for j in range(2,i):
                if i % j==0:
                    break
            else:
                tot_prime.append(i)


    print(sum(tot_prime))



sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sum_primes([2, 3, 4, 11, 20, 50, 71])
sum_primes([])