'''
835)A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
Create a function that determines whether a number is a Disarium or not.
Examples
is_disarium(75) ➞ False
# 7^1 + 5^2 = 7 + 25 = 32
is_disarium(135) ➞ True
# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
is_disarium(518) ➞ True
is_disarium(8) ➞ True'''


def is_disarium(num):
    tot=0
    j=1
    for i in str(num):
        tot+=int(str(i)) ** j
        j+=1
    print(tot==num)
    # print(tot)


is_disarium(75)
is_disarium(135)
is_disarium(518)
is_disarium(8)