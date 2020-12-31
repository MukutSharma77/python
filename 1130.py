'''How Many "Prime Numbers" Are There?
Create a function that finds how many prime numbers there are, up to the given integer.
Examples
prime_numbers(10) ➞ 4
# 2, 3, 5 and 7
prime_numbers(20) ➞ 8
# 2, 3, 5, 7, 11, 13, 17 and 19
prime_numbers(30) ➞ 10
# 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29'''

def prime_numbers(num):
    count_prime=0
    for i in range(2,num):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            count_prime+=1

    print(count_prime)

prime_numbers(10)
prime_numbers(20)
prime_numbers(30)