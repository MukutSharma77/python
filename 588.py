'''One Odd and One Even
Given a two digit number, return True if that number contains one even and one odd digit.
Examples
one_odd_one_even(12) ➞ True
one_odd_one_even(55) ➞ False
one_odd_one_even(22) ➞ False'''

num=81

count=0
while num:
    mod=num % 10
    if mod % 2==0:
        count+=1
    num//=10
if count==1:
    print(True)
else:
    print(False)