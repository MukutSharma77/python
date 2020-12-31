#Write a Python program to get numbers divisible by fifteen from a list using an anonymous function

list_=[1,2,3,15,7,6,8,30]

num=list(filter(lambda a:a%15==0,list_))
print(num)