'''Create a function where given the number n, return the sum of all square numbers up to and including n.
squares_sum(3) ➞ 14
# 1² + 2² + 3² =
# 1 + 4 + 9 =
# 14'''

num=int(input("Enter Number :   "))
number=0
for i in range(1,num+1):
    number+=i*i
print(number)