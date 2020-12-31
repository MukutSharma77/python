'''Write a function to check if a number is prime or not.'''

def check_prime(num):
    count=0
    for i in range(2,num):
        if num % i==0:
            count+=1

    if count==0:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is a not a prime number')


check_prime(5)
check_prime(10)
check_prime(7)
check_prime(101)
check_prime(17)
check_prime(50)
